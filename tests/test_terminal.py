"""Test illud.terminal."""
from unittest.mock import MagicMock, patch

import pytest

from illud.character import Character
from illud.inputs.standard_input import StandardInput
from illud.terminal import Terminal


def test_init() -> None:
    """Test illud.terminal.Terminal.__init__."""
    standard_input_mock = MagicMock(StandardInput)

    with patch('illud.terminal.StandardInput', return_value=standard_input_mock):

        terminal: Terminal = Terminal()

    assert terminal._standard_input == standard_input_mock  # pylint: disable=protected-access


# yapf: disable
@pytest.mark.parametrize('next_character, expected_character', [
    (Character('i'), Character('i')),
])
# yapf: enable
def test_get_character(next_character: Character, expected_character: Character) -> None:
    """Test illud.terminal.Terminal.get_character."""
    standard_input_mock = MagicMock(StandardInput, __next__=lambda self: next_character)

    with patch('illud.terminal.StandardInput', return_value=standard_input_mock):
        terminal: Terminal = Terminal()

        character: Character = terminal.get_character()

        assert character == expected_character
