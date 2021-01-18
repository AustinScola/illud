"""A mock terminal cursor."""
from unittest.mock import patch

from illud.integer_position_2d import IntegerPosition2D
from illud.terminal_cursor import TerminalCursor


def get_terminal_cursor_mock(position: IntegerPosition2D) -> TerminalCursor:
    """Return a terminal cursor with the given position."""
    with patch('illud.inputs.standard_input.StandardInput') as standard_input_mock, \
        patch('illud.outputs.standard_output.StandardOutput') as standard_output_mock, \
        patch('illud.terminal_cursor.TerminalCursor._get_position_from_terminal',
               return_value=position):
        terminal_cursor: TerminalCursor = TerminalCursor(standard_input_mock, standard_output_mock)
    return terminal_cursor
