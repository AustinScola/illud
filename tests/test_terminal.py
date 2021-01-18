"""Test illud.terminal."""
from unittest.mock import MagicMock, call, patch

import pytest

from illud.ansi.escape_codes.cursor import DEVICE_STATUS_REPORT
from illud.ansi.escape_codes.erase import CLEAR_SCREEN
from illud.character import Character
from illud.inputs.standard_input import StandardInput
from illud.integer_position_2d import IntegerPosition2D
from illud.outputs.standard_output import StandardOutput
from illud.terminal import Terminal
from illud.terminal_cursor import TerminalCursor
from mocks.terminal_cursor import get_terminal_cursor_mock


# yapf: disable
@pytest.mark.parametrize('cursor', [
    (get_terminal_cursor_mock(IntegerPosition2D(0, 0))),
])
# yapf: enable
def test_init(cursor: TerminalCursor) -> None:
    """Test illud.terminal.Terminal.__init__."""
    standard_input_mock = MagicMock(StandardInput)
    standard_output_mock = MagicMock(StandardOutput)

    with patch('illud.terminal.StandardInput', return_value=standard_input_mock), \
        patch('illud.terminal.StandardOutput', return_value=standard_output_mock), \
        patch('illud.terminal.TerminalCursor', return_value=cursor):

        terminal: Terminal = Terminal()

    assert terminal._standard_input == standard_input_mock  # pylint: disable=protected-access
    assert terminal._standard_output == standard_output_mock  # pylint: disable=protected-access
    assert terminal._cursor == cursor  # pylint: disable=protected-access


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


def test_clear_screen() -> None:
    """Test illud.terminal.Terminal.get_character."""
    standard_output_mock = MagicMock(StandardOutput)
    terminal: Terminal
    with patch('illud.terminal.StandardInput'), \
        patch('illud.terminal.StandardOutput', return_value=standard_output_mock):

        terminal = Terminal()

    terminal.clear_screen()

    standard_output_mock.write.assert_has_calls([call(DEVICE_STATUS_REPORT), call(CLEAR_SCREEN)])
    standard_output_mock.flush.assert_called_once()
