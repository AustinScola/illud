"""Test illud.terminal_cursor."""
from typing import Any
from unittest.mock import MagicMock, call, patch

import pytest
from seligimus.maths.integer_position_2d import IntegerPosition2D

from illud.ansi.escape_codes.cursor import HIDE_CURSOR, SHOW_CURSOR
from illud.outputs.standard_output import StandardOutput
from illud.terminal_cursor import TerminalCursor
from mocks.terminal_cursor import get_terminal_cursor_mock


def test_init() -> None:
    """Test illud.terminal_cursor.TerminalCursor.__init__."""
    standard_output_mock = MagicMock(StandardOutput)
    terminal_cursor: TerminalCursor = TerminalCursor(standard_output_mock)

    assert terminal_cursor._standard_output == standard_output_mock  # pylint: disable=protected-access


# yapf: disable
@pytest.mark.parametrize('terminal_cursor, other, expected_equality', [
    (get_terminal_cursor_mock(), 'foo', False),
    (get_terminal_cursor_mock(), get_terminal_cursor_mock(), True),
])
# yapf: enable
def test_eq(terminal_cursor: TerminalCursor, other: Any, expected_equality: bool) -> None:
    """Test illud.terminal_cursor.TerminalCursor.__eq__."""
    equality: bool = terminal_cursor == other

    assert equality == expected_equality


def test_hide() -> None:
    """Test illud.terminal_cursor.TerminalCursor.hide."""
    standard_output_mock = MagicMock()
    terminal_cursor: TerminalCursor = TerminalCursor(standard_output_mock)
    standard_output_mock.reset_mock()

    terminal_cursor.hide()

    standard_output_mock.write.assert_called_once_with(HIDE_CURSOR)


def test_show() -> None:
    """Test illud.terminal_cursor.TerminalCursor.show."""
    standard_output_mock = MagicMock()
    terminal_cursor: TerminalCursor = TerminalCursor(standard_output_mock)
    standard_output_mock.reset_mock()

    terminal_cursor.show()

    standard_output_mock.write.assert_called_once_with(SHOW_CURSOR)


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
    with patch('illud.outputs.standard_output.StandardOutput.write') as standard_output_write_mock:
        standard_output: StandardOutput = StandardOutput()

        terminal_cursor: TerminalCursor = TerminalCursor(standard_output)
        terminal_cursor.move(position)

        standard_output_write_mock.assert_has_calls([call(expected_output)])
