"""Test illud.terminal."""
import itertools
import os
from typing import Optional
from unittest.mock import MagicMock, patch

import pytest
from seligimus.maths.integer_position_2d import IntegerPosition2D
from seligimus.maths.integer_size_2d import IntegerSize2D

from illud.ansi.escape_codes.erase import CLEAR_SCREEN
from illud.buffer import Buffer
from illud.character import Character
from illud.cursor import Cursor
from illud.inputs.standard_input import StandardInput
from illud.outputs.standard_output import StandardOutput
from illud.terminal import Terminal
from illud.terminal_cursor import TerminalCursor
from illud.window import Window


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

        terminal_cursor_contructor.assert_called_once_with(standard_input_mock,
                                                           standard_output_mock)

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


def test_clear_screen() -> None:
    """Test illud.terminal.Terminal.get_character."""
    standard_output_mock = MagicMock(StandardOutput)
    terminal: Terminal
    with patch('illud.terminal.StandardInput'), \
        patch('illud.terminal.StandardOutput', return_value=standard_output_mock):

        terminal = Terminal()

    terminal.clear_screen()

    assert standard_output_mock.write.call_args[0] == (CLEAR_SCREEN, )


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('window, cursor, expected_output', [
    (Window(IntegerPosition2D(), IntegerSize2D(0, 0), Buffer()), None, ''),
    (Window(IntegerPosition2D(), IntegerSize2D(1, 1), Buffer()), None, '\x1b[;H '),
    (Window(IntegerPosition2D(), IntegerSize2D(2, 1), Buffer()), None, '\x1b[;H  '),
    (Window(IntegerPosition2D(), IntegerSize2D(3, 1), Buffer()), None, '\x1b[;H   '),
    (Window(IntegerPosition2D(), IntegerSize2D(1, 2), Buffer()), None, '\x1b[;H \x1b[2;H '),
    (Window(IntegerPosition2D(), IntegerSize2D(2, 2), Buffer()), None, '\x1b[;H  \x1b[2;H  '),
    (Window(IntegerPosition2D(), IntegerSize2D(2, 1), Buffer('foo')), None, '\x1b[;Hfo'),
    (Window(IntegerPosition2D(), IntegerSize2D(3, 1), Buffer('foo')), None, '\x1b[;Hfoo'),
    (Window(IntegerPosition2D(), IntegerSize2D(5, 1), Buffer('foo')), None, '\x1b[;Hfoo  '),
    (Window(IntegerPosition2D(), IntegerSize2D(5, 1), Buffer('foo\n')), None, '\x1b[;Hfoo  '),
    (Window(IntegerPosition2D(), IntegerSize2D(1, 2), Buffer('f')), None, '\x1b[;Hf\x1b[2;H '),
    (Window(IntegerPosition2D(), IntegerSize2D(1, 2), Buffer('f\nb')), None, '\x1b[;Hf\x1b[2;Hb'),
    (Window(IntegerPosition2D(), IntegerSize2D(1, 2), Buffer('foo\nb')), None, '\x1b[;Hf\x1b[2;Hb'),
    (Window(IntegerPosition2D(), IntegerSize2D(1, 2), Buffer('foo\nbar')), None, '\x1b[;Hf\x1b[2;Hb'),
    (Window(IntegerPosition2D(), IntegerSize2D(2, 2), Buffer('f\nb')), None, '\x1b[;Hf \x1b[2;Hb '),
    (Window(IntegerPosition2D(), IntegerSize2D(5, 2), Buffer('foo\nbar')), None, '\x1b[;Hfoo  \x1b[2;Hbar  '),
    (Window(IntegerPosition2D(), IntegerSize2D(5, 2), Buffer('foo\nbar')), None, '\x1b[;Hfoo  \x1b[2;Hbar  '),
    (Window(IntegerPosition2D(), IntegerSize2D(5, 3), Buffer('foo\nbar\nbaz')), None, '\x1b[;Hfoo  \x1b[2;Hbar  \x1b[3;Hbaz  '),
    (Window(IntegerPosition2D(), IntegerSize2D(0, 0), Buffer()), Cursor(Buffer(), 0), ''),
    (Window(IntegerPosition2D(), IntegerSize2D(1, 1), Buffer('')), Cursor(Buffer(''), 0), '\x1b[;H\x1b[7m \x1b[m'),
    (Window(IntegerPosition2D(), IntegerSize2D(4, 1), Buffer('foo')), Cursor(Buffer(''), 3), '\x1b[;Hfoo\x1b[7m \x1b[m'),
    (Window(IntegerPosition2D(), IntegerSize2D(3, 1), Buffer('   ')), Cursor(Buffer('   '), 0), '\x1b[;H\x1b[7m \x1b[m  '),
    (Window(IntegerPosition2D(), IntegerSize2D(3, 1), Buffer('   ')), Cursor(Buffer('   '), 1), '\x1b[;H \x1b[7m \x1b[m '),
    (Window(IntegerPosition2D(), IntegerSize2D(3, 1), Buffer('foo')), Cursor(Buffer('foo'), 0), '\x1b[;H\x1b[7mf\x1b[moo'),
])
# yapf: enable # pylint: enable=line-too-long
def test_draw_window(window: Window, cursor: Optional[Cursor], expected_output: str) -> None:
    """Test illud.terminal.Terminal.draw_window."""
    standard_output_mock = MagicMock(StandardOutput)
    with patch('illud.terminal.StandardInput'), \
        patch('illud.terminal.StandardOutput', return_value=standard_output_mock), \
        patch('illud.terminal_cursor.TerminalCursor._get_position_from_terminal'):

        terminal: Terminal = Terminal()

        standard_output_mock.write.reset_mock()

        terminal.draw_window(window, cursor)

    calls_args = itertools.chain.from_iterable(
        call_args for call_args, _ in standard_output_mock.write.call_args_list)
    output: str = ''.join(calls_args)

    assert output == expected_output

    if expected_output:
        standard_output_mock.flush.assert_called_once()
