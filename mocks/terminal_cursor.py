"""A mock terminal cursor."""
from unittest.mock import MagicMock

from illud.outputs.standard_output import StandardOutput
from illud.terminal_cursor import TerminalCursor


def get_terminal_cursor_mock() -> TerminalCursor:
    """Return a terminal cursor with the given position."""
    standard_output_mock = MagicMock(StandardOutput)
    terminal_cursor: TerminalCursor = TerminalCursor(standard_output_mock)

    return terminal_cursor
