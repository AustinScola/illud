"""Test illud.inputs.standard_input."""
import sys
import termios
from unittest.mock import MagicMock, patch

import pytest

from illud.character import Character, CharacterIterator
from illud.input import Input
from illud.inputs.standard_input import StandardInput, TeletypeAttributes


def test_inheritance() -> None:
    """Test illud.inputs.standard_input.StandardInput inheritance."""
    assert issubclass(StandardInput, Input)


ATTRIBUTES = [
    17664, 5, 191, 35387, 15, 15,
    [
        b'\x03', b'\x1c', b'\x7f', b'\x15', b'\x04', b'\x00', b'\x01', b'\x00', b'\x11', b'\x13',
        b'\x1a', b'\x00', b'\x12', b'\x0f', b'\x17', b'\x16', b'\x00', b'\x00', b'\x00', b'\x00',
        b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00',
        b'\x00', b'\x00'
    ]
]


# yapf: disable
@pytest.mark.parametrize('standard_input_file_number, attributes_before', [
    (1, ATTRIBUTES),
])
# yapf: enable
def test_init(standard_input_file_number: int, attributes_before: TeletypeAttributes) -> None:
    """Test illud.inputs.standard_input.StandardInput.__init__."""
    with patch('sys.stdin', fileno=lambda: standard_input_file_number) as stdin_mock, \
        patch.object(StandardInput, '_get_attributes', return_value=attributes_before), \
        patch.object(StandardInput, '_use_raw_mode') as use_set_raw_mock:

        standard_input: StandardInput = StandardInput()

        assert standard_input._stdin == stdin_mock  # pylint: disable=protected-access
        assert standard_input._attributes_before == attributes_before  # pylint: disable=protected-access
        use_set_raw_mock.assert_called_once()


# yapf: disable
@pytest.mark.parametrize('current_attributes, expected_attributes', [
    (ATTRIBUTES, ATTRIBUTES),
])
# yapf: enable
def test_get_attributes(current_attributes: TeletypeAttributes,
                        expected_attributes: TeletypeAttributes) -> None:
    """Test illud.inputs.standard_input.StandardInput._get_attributes."""
    stdin_mock = MagicMock(sys.stdin)
    standard_input_mock = MagicMock(StandardInput, _stdin=stdin_mock)

    with patch('termios.tcgetattr', autospec=True, return_value=current_attributes):
        attributes: TeletypeAttributes = StandardInput._get_attributes(standard_input_mock)  # pylint: disable=protected-access

    assert attributes == expected_attributes


# yapf: disable
@pytest.mark.parametrize('standard_input_file_number', [
    (1),
])
# yapf: enable
def test_use_raw_mode(standard_input_file_number: int) -> None:
    """Test illud.inputs.standard_input.StandardInput._use_raw_mode."""
    stdin_mock = MagicMock(sys.stdin, fileno=lambda: standard_input_file_number)
    standard_input_mock = MagicMock(StandardInput, _stdin=stdin_mock)

    with patch('tty.setraw', autospec=True) as setraw_mock:
        StandardInput._use_raw_mode(standard_input_mock)  # pylint: disable=protected-access

        setraw_mock.assert_called_once_with(standard_input_file_number)


# yapf: disable
@pytest.mark.parametrize('standard_input_file_number, stdin, expected_next_input', [
    (1, 'i', Character('i')),
])
# yapf: enable
def test_next(standard_input_file_number: int, stdin: str, expected_next_input: Character) -> None:
    """Test illud.inputs.standard_input.StandardInput.__next__."""
    stdin_mock = MagicMock(sys.stdin,
                           read=lambda n: stdin,
                           fileno=lambda: standard_input_file_number)
    standard_input_mock = MagicMock(StandardInput,
                                    _stdin=stdin_mock,
                                    __next__=StandardInput.__next__)

    next_input: Character = next(standard_input_mock)

    assert next_input == expected_next_input


# yapf: disable
@pytest.mark.parametrize('next_character', [
    (Character('i')),
])
# yapf: enable
def test_iter(next_character: Character) -> None:
    """Test illud.inputs.standard_input.StandardInput.__iter__."""
    next_mock = MagicMock(return_value=next_character)
    standard_input_mock = MagicMock(StandardInput,
                                    __next__=next_mock,
                                    __iter__=StandardInput.__iter__)

    with pytest.raises(NotImplementedError):
        characters: CharacterIterator = iter(standard_input_mock)

        assert next(characters) == next_character


def test_del() -> None:
    """Test illud.inputs.standard_input.StandardInput.__del__."""
    standard_input_mock = MagicMock(StandardInput, autospec=True)

    StandardInput.__del__(standard_input_mock)

    standard_input_mock._reset_attributes.assert_called_once()  # pylint: disable=protected-access


# yapf: disable
@pytest.mark.parametrize('standard_input_file_number, attributes_before', [
    (1, ATTRIBUTES),
])
# yapf: enable
def test_reset_attributes(standard_input_file_number: int,
                          attributes_before: TeletypeAttributes) -> None:
    """Test illud.inputs.standard_input.StandardInput._reset_attributes."""
    stdin_mock = MagicMock(sys.stdin, fileno=lambda: standard_input_file_number)
    standard_input_mock = MagicMock(StandardInput,
                                    _stdin=stdin_mock,
                                    _attributes_before=attributes_before)

    with patch('termios.tcsetattr', autospec=True) as tcsetattr_mock:
        StandardInput._reset_attributes(standard_input_mock)  # pylint: disable=protected-access

        tcsetattr_mock.assert_called_once_with(stdin_mock, termios.TCSADRAIN, attributes_before)
