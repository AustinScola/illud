"""Test illud.illud."""
import itertools
from typing import Any, Dict, Optional
from unittest.mock import MagicMock, patch

import pytest
from seligimus.maths.integer_size_2d import IntegerSize2D

from illud.ansi.escape_codes.cursor import MOVE_CURSOR_HOME
from illud.ansi.escape_codes.erase import CLEAR_SCREEN
from illud.buffer import Buffer
from illud.character import Character
from illud.command import Command
from illud.exceptions.quit_exception import QuitException
from illud.illud import Illud
from illud.illud_state import IlludState
from illud.modes.insert import Insert
from illud.outputs.standard_output import StandardOutput
from illud.repl import REPL
from illud.terminal import Terminal


def test_inheritance() -> None:
    """Test illud.illud.Illud inheritance."""
    assert issubclass(Illud, REPL)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('illud_initial_state, pass_illud_initial_state, terminal_size, expected_illud_state', [
    (None, False, IntegerSize2D(0, 0), IlludState(terminal_size=IntegerSize2D(0, 0))),
    (None, False, IntegerSize2D(120, 80), IlludState(terminal_size=IntegerSize2D(120, 80))),
    (IlludState(), True, None, IlludState()),
    (IlludState(Buffer('foo')), True, None, IlludState(Buffer('foo'))),
])
# yapf: enable # pylint: enable=line-too-long
def test_init(illud_initial_state: Optional[IlludState], pass_illud_initial_state: bool,
              terminal_size: Optional[IntegerSize2D], expected_illud_state: IlludState) -> None:
    """Test illud.illud.Illud.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_illud_initial_state:
        keyword_arguments['initial_state'] = illud_initial_state

    terminal_get_size_mock = MagicMock(return_value=terminal_size)
    terminal_mock = MagicMock(get_size=terminal_get_size_mock)
    with patch('illud.illud.Terminal', return_value=terminal_mock):

        illud: Illud = Illud(**keyword_arguments)

        assert illud._terminal == terminal_mock  # pylint: disable=protected-access

        assert illud._state == expected_illud_state  # pylint: disable=protected-access


def test_startup() -> None:
    """Test illud.illud.Illud.startup."""
    clear_screen_mock = MagicMock()
    terminal_mock = MagicMock(Terminal, autospec=True, clear_screen=clear_screen_mock)
    with patch('illud.illud.Terminal', return_value=terminal_mock), \
        patch('illud.illud.Illud.print') as print_mock:

        illud: Illud = Illud()

        illud.startup()

        clear_screen_mock.assert_called_once()
        print_mock.assert_called_once_with(None)


# yapf: disable
@pytest.mark.parametrize('character, expected_command', [
    (Character('i'), Command(Character('i'))),
])
# yapf: enable
def test_read(character: Character, expected_command: Command) -> None:
    """Test illud.illud.Illud.read."""
    terminal_mock = MagicMock(get_character=lambda: character)

    with patch('illud.illud.Terminal', return_value=terminal_mock):
        illud: Illud = Illud()

        command: Command = illud.read()

    assert command == expected_command


# yapf: disable
@pytest.mark.parametrize('initial_state, input_, expected_state_after', [
    (IlludState(), Command(Character('i')), IlludState(mode=Insert())),
])
# yapf: enable
def test_evaluate(initial_state: IlludState, input_: Command,
                  expected_state_after: IlludState) -> None:
    """Test illud.illud.Illud.evaluate."""

    with patch('illud.illud.Terminal'):
        illud: Illud = Illud(initial_state)

    illud.evaluate(input_)

    assert illud._state == expected_state_after  # pylint: disable=protected-access


# yapf: disable
@pytest.mark.parametrize('illud_state, result, expected_output', [
    (IlludState(terminal_size=IntegerSize2D(1, 1)), None, '\x1b[;H\x1b[7m \x1b[m'),
    (IlludState(Buffer('foo'), terminal_size=IntegerSize2D(3, 1)), None, '\x1b[;H\x1b[7mf\x1b[moo'),
    (IlludState(Buffer('foo'), cursor_position=1, terminal_size=IntegerSize2D(3, 1)), None, '\x1b[;Hf\x1b[7mo\x1b[mo'),
])
# yapf: enable
def test_print(illud_state: IlludState, result: Any, expected_output: str) -> None:
    """Test illud.illud.Illud.print."""
    standard_output_mock = MagicMock(StandardOutput)
    with patch('illud.terminal.StandardInput'), \
        patch('illud.terminal.StandardOutput', return_value=standard_output_mock), \
        patch('illud.terminal.Terminal.clear_screen'), \
        patch('illud.terminal_cursor.TerminalCursor._get_position_from_terminal'):

        illud: Illud = Illud(illud_state)
        standard_output_mock.write.reset_mock()

    illud.print(result)

    calls_args = itertools.chain.from_iterable(
        call_args for call_args, _ in standard_output_mock.write.call_args_list)
    output: str = ''.join(calls_args)

    assert list(output) == list(expected_output)
    standard_output_mock.flush.assert_called_once()


# yapf: disable
@pytest.mark.parametrize('exception, expect_reraises, expect_exits, expected_output', [
    (Exception(), True, False, None),
    (TypeError(), True, False, None),
    (QuitException(), False, True, CLEAR_SCREEN + MOVE_CURSOR_HOME),
])
# yapf: enable
def test_catch(exception: Exception, expect_reraises: bool, expect_exits: bool,
               expected_output: Optional[str]) -> None:
    """Test illud.illud.Illud.catch."""
    standard_output_mock = MagicMock(StandardOutput)
    with patch('illud.terminal.StandardInput'), \
        patch('illud.terminal.StandardOutput', return_value=standard_output_mock), \
        patch('illud.terminal_cursor.TerminalCursor._get_position_from_terminal'):

        terminal_mock = Terminal()
        standard_output_mock.write.reset_mock()

    with patch('illud.illud.Terminal', return_value=terminal_mock):
        with patch('illud.terminal.Terminal.get_size'):
            illud: Illud = Illud()
        standard_output_mock.write.reset_mock()

    if expect_reraises:
        with pytest.raises(type(exception)):
            illud.catch(exception)
    elif expect_exits:
        with pytest.raises(SystemExit):
            illud.catch(exception)

    calls_args = itertools.chain.from_iterable(
        call_args for call_args, _ in standard_output_mock.write.call_args_list)
    output: str = ''.join(calls_args)

    if expected_output is not None:
        assert list(output) == list(expected_output)
    else:
        standard_output_mock.write.assert_not_called()
