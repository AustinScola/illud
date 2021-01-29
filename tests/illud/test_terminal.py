"""Test illud.terminal."""
from unittest.mock import MagicMock, call, patch

import pytest
from pytest import CaptureFixture

from illud.ansi.escape_codes.cursor import DEVICE_STATUS_REPORT
from illud.ansi.escape_codes.erase import CLEAR_SCREEN
from illud.buffer import Buffer
from illud.character import Character
from illud.inputs.standard_input import StandardInput
from illud.math.integer_position_2d import IntegerPosition2D
from illud.outputs.standard_output import StandardOutput
from illud.terminal import Terminal
from illud.terminal_cursor import TerminalCursor
from illud.window import Window
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
    assert len(standard_output_mock.flush.mock_calls) == 2


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('window, expected_output', [
    (Window(IntegerPosition2D(0, 0), 0, 0, Buffer()), ''),
    (Window(IntegerPosition2D(0, 0), 1, 1, Buffer()), '\x1b[;H '),
    (Window(IntegerPosition2D(0, 0), 2, 1, Buffer()), '\x1b[;H  '),
    (Window(IntegerPosition2D(0, 0), 3, 1, Buffer()), '\x1b[;H   '),
    (Window(IntegerPosition2D(0, 0), 1, 2, Buffer()), '\x1b[;H \x1b[2;H '),
    (Window(IntegerPosition2D(0, 0), 2, 2, Buffer()), '\x1b[;H  \x1b[2;H  '),
    (Window(IntegerPosition2D(0, 0), 2, 1, Buffer('foo')), '\x1b[;Hfo'),
    (Window(IntegerPosition2D(0, 0), 3, 1, Buffer('foo')), '\x1b[;Hfoo'),
    (Window(IntegerPosition2D(0, 0), 5, 1, Buffer('foo')), '\x1b[;Hfoo  '),
    (Window(IntegerPosition2D(0, 0), 5, 1, Buffer('foo\n')), '\x1b[;Hfoo  '),
    (Window(IntegerPosition2D(0, 0), 1, 2, Buffer('f')), '\x1b[;Hf\x1b[2;H '),
    (Window(IntegerPosition2D(0, 0), 1, 2, Buffer('f\nb')), '\x1b[;Hf\x1b[2;Hb'),
    (Window(IntegerPosition2D(0, 0), 1, 2, Buffer('foo\nb')), '\x1b[;Hf\x1b[2;Hb'),
    (Window(IntegerPosition2D(0, 0), 1, 2, Buffer('foo\nbar')), '\x1b[;Hf\x1b[2;Hb'),
    (Window(IntegerPosition2D(0, 0), 2, 2, Buffer('f\nb')), '\x1b[;Hf \x1b[2;Hb '),
    (Window(IntegerPosition2D(0, 0), 5, 2, Buffer('foo\nbar')), '\x1b[;Hfoo  \x1b[2;Hbar  '),
    (Window(IntegerPosition2D(0, 0), 5, 2, Buffer('foo\nbar')), '\x1b[;Hfoo  \x1b[2;Hbar  '),
    (Window(IntegerPosition2D(0, 0), 5, 3, Buffer('foo\nbar\nbaz')), '\x1b[;Hfoo  \x1b[2;Hbar  \x1b[3;Hbaz  '),
])
# yapf: enable # pylint: enable=line-too-long
def test_draw_window(capsys: CaptureFixture, window: Window, expected_output: str) -> None:
    """Test illud.terminal.Terminal.draw_window."""
    with patch('illud.terminal.StandardInput'), \
        patch('illud.terminal_cursor.TerminalCursor._get_position_from_terminal'):

        terminal: Terminal = Terminal()

        terminal.draw_window(window)

    captured_output: str = capsys.readouterr().out
    # NOTE: Use a list here because otherwise pytest will print out the actual ANSI escape codes and
    # then the console ouput of pytest is garbled.
    assert list(expected_output) == list(captured_output)
