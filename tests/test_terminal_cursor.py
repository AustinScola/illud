"""Test illud.terminal_cursor."""
from io import StringIO
from unittest.mock import MagicMock, call, patch

import pytest

from illud.ansi.escape_codes.cursor import DEVICE_STATUS_REPORT
from illud.inputs.standard_input import StandardInput
from illud.integer_position_2d import IntegerPosition2D
from illud.outputs.standard_output import StandardOutput
from illud.terminal_cursor import TerminalCursor


# yapf: disable
@pytest.mark.parametrize('position, expected_position', [
    (IntegerPosition2D(0, 0), IntegerPosition2D(0, 0)),
])
# yapf: enable
def test_init(position: IntegerPosition2D, expected_position: IntegerPosition2D) -> None:
    """Test illud.terminal_cursor.TerminalCursor.__init__."""
    standard_input_mock = MagicMock(StandardInput)
    standard_output_mock = MagicMock(StandardOutput)
    with patch('illud.terminal_cursor.TerminalCursor._get_position_from_terminal',
               return_value=position):
        terminal_cursor: TerminalCursor = TerminalCursor(standard_input_mock, standard_output_mock)

    assert terminal_cursor._position == expected_position  # pylint: disable=protected-access
    assert terminal_cursor._standard_input == standard_input_mock  # pylint: disable=protected-access
    assert terminal_cursor._standard_output == standard_output_mock  # pylint: disable=protected-access


# yapf: disable
@pytest.mark.parametrize('cursor_position_report, expected_position', [
    (';R', IntegerPosition2D(0, 0)),
    ('1;R', IntegerPosition2D(0, 1)),
    (';1R', IntegerPosition2D(1, 0)),
    ('1;1R', IntegerPosition2D(1, 1)),
])
# yapf: enable
def test_get_position_from_terminal(cursor_position_report: str,
                                    expected_position: IntegerPosition2D) -> None:
    """Test illud.terminal_cursor.TerminalCursor._get_position_from_terminal."""
    with patch('sys.stdin', StringIO(cursor_position_report)), \
        patch.object(StandardInput, '_get_attributes'), \
        patch.object(StandardInput, '_use_raw_mode'):

        standard_input: StandardInput = StandardInput()

    with patch('illud.outputs.standard_output.StandardOutput.write') as standard_output_write_mock:
        standard_output: StandardOutput = StandardOutput()

        with patch('illud.terminal_cursor.TerminalCursor._get_position_from_terminal'):
            terminal_cursor: TerminalCursor = TerminalCursor(standard_input, standard_output)

        position: IntegerPosition2D = terminal_cursor._get_position_from_terminal()  # pylint: disable=protected-access

        assert position == expected_position
        standard_output_write_mock.assert_called_once_with(DEVICE_STATUS_REPORT)


# yapf: disable
@pytest.mark.parametrize('position, expected_output', [
    (IntegerPosition2D(0,0), '\x1b[;H'),
    (IntegerPosition2D(0,1), '\x1b[2;H'),
    (IntegerPosition2D(1,0), '\x1b[;2H'),
    (IntegerPosition2D(1,1), '\x1b[2;2H'),
    (IntegerPosition2D(1,7), '\x1b[8;2H'),
    (IntegerPosition2D(7,1), '\x1b[2;8H'),
    (IntegerPosition2D(7,7), '\x1b[8;8H'),
])
# yapf: enable
def test_move(position: IntegerPosition2D, expected_output: str) -> None:
    """Test illud.terminal_cursor.TerminalCursor.move."""
    standard_input: StandardInput = MagicMock(StandardInput)

    with patch('illud.outputs.standard_output.StandardOutput.write') as standard_output_write_mock:
        standard_output: StandardOutput = StandardOutput()

        terminal_cursor: TerminalCursor = TerminalCursor(standard_input, standard_output)
        terminal_cursor.move(position)

        standard_output_write_mock.assert_has_calls(
            [call(DEVICE_STATUS_REPORT), call(expected_output)])
        assert terminal_cursor._position == position  # pylint: disable=protected-access
