"""Test illud.terminal."""
import os
from unittest.mock import MagicMock, patch

import pytest
from seligimus.maths.integer_size_2d import IntegerSize2D

from illud.ansi.escape_codes.cursor import MOVE_CURSOR_HOME
from illud.ansi.escape_codes.erase import CLEAR_SCREEN
from illud.ansi.escape_codes.screen import DISABLE_ALTERNATIVE_SCREEN, ENABLE_ALTERNATIVE_SCREEN
from illud.character import Character
from illud.inputs.standard_input import StandardInput
from illud.outputs.standard_output import StandardOutput
from illud.terminal import Terminal
from illud.terminal_cursor import TerminalCursor


def test_init() -> None:
    """Test illud.terminal.Terminal.__init__."""
    standard_input_mock = MagicMock(StandardInput)
    standard_output_mock = MagicMock(StandardOutput)
    terminal_cursor_mock = MagicMock(TerminalCursor)

    with patch('illud.terminal.StandardInput', return_value=standard_input_mock), \
        patch('illud.terminal.StandardOutput', return_value=standard_output_mock), \
        patch('illud.terminal.TerminalCursor', return_value=terminal_cursor_mock) as \
            terminal_cursor_contructor:

        terminal: Terminal = Terminal()

        terminal_cursor_contructor.assert_called_once_with(standard_output_mock)

    assert terminal._standard_input == standard_input_mock  # pylint: disable=protected-access
    assert terminal._standard_output == standard_output_mock  # pylint: disable=protected-access
    assert terminal._cursor == terminal_cursor_mock  # pylint: disable=protected-access
    terminal_cursor_mock.hide.assert_called_once()


# yapf: disable
@pytest.mark.parametrize('mock_terminal_size, expected_size', [
    (os.terminal_size([0, 0]), IntegerSize2D(0, 0)),
    (os.terminal_size([1, 1]), IntegerSize2D(1, 1)),
    (os.terminal_size([3, 7]), IntegerSize2D(3, 7)),
])
# yapf: enable
def test_get_size(mock_terminal_size: os.terminal_size, expected_size: IntegerSize2D) -> None:
    """Test illud.terminal.Terminal.get_size."""
    with patch('illud.terminal.StandardInput'), patch('illud.terminal.StandardOutput'):
        terminal: Terminal = Terminal()

    with patch('os.get_terminal_size', return_value=mock_terminal_size):
        size: IntegerSize2D = terminal.get_size()

    assert size == expected_size


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


def test_enable_alternative_screen() -> None:
    """Test illud.terminal.Terminal.enable_alternative_screen."""
    standard_output_mock = MagicMock(StandardOutput)
    terminal: Terminal
    with patch('illud.terminal.StandardInput'), \
        patch('illud.terminal.StandardOutput', return_value=standard_output_mock):

        terminal = Terminal()

    terminal.enable_alternative_screen()

    assert standard_output_mock.write.call_args[0] == (ENABLE_ALTERNATIVE_SCREEN, )


def test_disable_alternative_screen() -> None:
    """Test illud.terminal.Terminal.disable_alternative_screen."""
    standard_output_mock = MagicMock(StandardOutput)
    terminal: Terminal
    with patch('illud.terminal.StandardInput'), \
        patch('illud.terminal.StandardOutput', return_value=standard_output_mock):

        terminal = Terminal()

    terminal.disable_alternative_screen()

    assert standard_output_mock.write.call_args[0] == (DISABLE_ALTERNATIVE_SCREEN, )


def test_clear_screen() -> None:
    """Test illud.terminal.Terminal.clear_screen."""
    standard_output_mock = MagicMock(StandardOutput)
    terminal: Terminal
    with patch('illud.terminal.StandardInput'), \
        patch('illud.terminal.StandardOutput', return_value=standard_output_mock):

        terminal = Terminal()

    terminal.clear_screen()

    assert standard_output_mock.write.call_args[0] == (CLEAR_SCREEN, )


def test_move_cursor_home() -> None:
    """Test illud.terminal.Terminal.move_cursor_home."""
    standard_output_mock = MagicMock(StandardOutput)
    terminal: Terminal
    with patch('illud.terminal.StandardInput'), \
        patch('illud.terminal.StandardOutput', return_value=standard_output_mock):

        terminal = Terminal()

    terminal.move_cursor_home()

    assert standard_output_mock.write.call_args[0] == (MOVE_CURSOR_HOME, )


def test_update() -> None:
    """Test illud.terminal.Terminal.draw_update."""
    standard_output_mock = MagicMock(StandardOutput, autospec=True)
    with patch('illud.terminal.StandardInput'), \
        patch('illud.terminal.StandardOutput', return_value=standard_output_mock):

        terminal: Terminal = Terminal()
        standard_output_mock.flush.reset_mock()

        terminal.update()

    standard_output_mock.flush.assert_called_once()
