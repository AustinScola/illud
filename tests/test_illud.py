"""Test illud.illud."""
import itertools
from typing import Any, Dict, Optional
from unittest.mock import MagicMock, patch

import pytest
from seligimus.maths.integer_position_2d import IntegerPosition2D
from seligimus.maths.integer_size_2d import IntegerSize2D

from illud.ansi.escape_codes.cursor import SHOW_CURSOR
from illud.ansi.escape_codes.screen import DISABLE_ALTERNATIVE_SCREEN
from illud.buffer import Buffer
from illud.canvas import Canvas
from illud.character import Character
from illud.cursor import Cursor
from illud.exceptions.quit_exception import QuitException
from illud.illud import Illud
from illud.illud_input import IlludInput
from illud.illud_state import IlludState
from illud.inputs.signal_listener import SignalListener
from illud.inputs.standard_input import StandardInput
from illud.modes.insert import Insert
from illud.modes.select import Select
from illud.outputs.standard_output import StandardOutput
from illud.repl import REPL
from illud.selection import Selection
from illud.signal_ import Signals
from illud.signal_handler import SignalHandler
from illud.signals.terminal_size_change import TerminalSizeChange
from illud.status_bar import StatusBar
from illud.terminal import Terminal
from illud.window import Window


def test_inheritance() -> None:
    """Test illud.illud.Illud inheritance."""
    assert issubclass(Illud, REPL)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('illud_initial_state, pass_illud_initial_state, terminal_size, expected_illud_state', [
    (None, False, IntegerSize2D(0, 0), IlludState(terminal_size=IntegerSize2D(0, 0))),
    (None, False, IntegerSize2D(120, 80), IlludState(terminal_size=IntegerSize2D(120, 80))),
    (IlludState(), True, None, IlludState()),
    (IlludState(buffer_=Buffer('foo')), True, None, IlludState(buffer_=Buffer('foo'))),
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
        assert isinstance(illud._signal_listener, SignalListener)  # pylint: disable=protected-access
        assert not illud._signal_listener  # pylint: disable=protected-access
        assert isinstance(illud._signal_handler, SignalHandler)  # pylint: disable=protected-access

        assert illud._state == expected_illud_state  # pylint: disable=protected-access


def test_startup() -> None:
    """Test illud.illud.Illud.startup."""
    enable_alternative_screen_mock = MagicMock()
    terminal_mock = MagicMock(Terminal,
                              autospec=True,
                              enable_alternative_screen=enable_alternative_screen_mock)
    with patch('illud.illud.Terminal', return_value=terminal_mock), \
        patch('illud.illud.Illud.print') as print_mock, \
        patch('illud.illud.SignalListener.start') as signal_listener_start_mock:

        illud: Illud = Illud()

        illud.startup()

        enable_alternative_screen_mock.assert_called_once()
        print_mock.assert_called_once_with(None)
        signal_listener_start_mock.assert_called_once()


@pytest.mark.parametrize('signals, character, expected_input', [
    ([], Character('i'), Character('i')),
    ([TerminalSizeChange()], Character('i'), TerminalSizeChange()),
])
# yapf: enable
def test_read(signals: Signals, character: Character, expected_input: IlludInput) -> None:
    """Test illud.illud.Illud.read."""
    signal_listener: SignalListener = SignalListener()
    for signal in signals:
        signal_listener._signals.put_nowait(signal)  # pylint: disable=protected-access

    terminal_mock = MagicMock(get_character=lambda: character)

    with patch('illud.illud.Terminal', return_value=terminal_mock), \
        patch('illud.illud.SignalListener', return_value=signal_listener):
        illud: Illud = Illud()

        input_: IlludInput = illud.read()

    assert input_ == expected_input


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('initial_state, input_, terminal_size, expected_state_after', [
    (IlludState(), Character('i'), None, IlludState(mode=Insert(), status_bar=StatusBar(buffer_=Buffer('Insert')))),
    (IlludState(), TerminalSizeChange(), IntegerSize2D(120, 80), IlludState(window=Window(size=IntegerSize2D(120, 80)), canvas=Canvas(IntegerSize2D(120, 80)).fill(' '), terminal_size=IntegerSize2D(120, 80))),
])
# yapf: enable # pylint: enable=line-too-long
def test_evaluate(initial_state: IlludState, input_: IlludInput,
                  terminal_size: Optional[IntegerSize2D], expected_state_after: IlludState) -> None:
    """Test illud.illud.Illud.evaluate."""
    with patch('illud.illud.Terminal'), \
        patch('illud.signal_handler.Terminal.get_size', return_value=terminal_size):

        illud: Illud = Illud(initial_state)

        illud.evaluate(input_)

    assert illud._state == expected_state_after  # pylint: disable=protected-access


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('illud_state, result, expected_output', [
    (IlludState(window=Window(size=IntegerSize2D(1, 1)), canvas=Canvas(IntegerSize2D(1, 1), [[' ']])), None, '\x1b[;H \x1b[;H\x1b[7m \x1b[;2H\x1b[m'),
    (IlludState(cursor=Cursor(Buffer('foo')), window=Window(size=IntegerSize2D(3, 1), buffer_=Buffer('foo')), canvas=Canvas(IntegerSize2D(3, 1), [[' ', ' ', ' ']])), None, '\x1b[;Hfoo\x1b[;H\x1b[7mf\x1b[;2H\x1b[m'),
    (IlludState(cursor=Cursor(Buffer('foo'), 1), window=Window(size=IntegerSize2D(3, 1), buffer_=Buffer('foo')), canvas=Canvas(IntegerSize2D(3, 1), [[' ', ' ', ' ']], inversions=[IntegerPosition2D()])), None, '\x1b[;Hfoo\x1b[;2H\x1b[7mo\x1b[;3H\x1b[m'),
    (IlludState(mode=Select(), selection=Selection(Buffer('foo'), 1), window=Window(size=IntegerSize2D(3, 1), buffer_=Buffer('foo')), canvas=Canvas(IntegerSize2D(3, 1), [[' ', ' ', ' ']], inversions=[IntegerPosition2D()])), None, '\x1b[;Hfoo\x1b[;2H\x1b[7mo\x1b[;3H\x1b[m'),
    (IlludState(window=Window(size=IntegerSize2D(3, 2)), status_bar=StatusBar(position=IntegerPosition2D(0, 2), size=IntegerSize2D(3, 1)), canvas=Canvas(IntegerSize2D(3, 3))), None, '\x1b[;H   \x1b[2;H   \x1b[3;H   \x1b[;H\x1b[7m \x1b[;2H\x1b[m\x1b[3;H\x1b[7m \x1b[3;2H\x1b[m\x1b[3;2H\x1b[7m \x1b[3;3H\x1b[m\x1b[3;3H\x1b[7m \x1b[3;4H\x1b[m'),
])
# yapf: enable # pylint: enable=line-too-long
def test_print(illud_state: IlludState, result: Any, expected_output: str) -> None:
    """Test illud.illud.Illud.print."""
    standard_output_mock = MagicMock(StandardOutput)
    illud_state.canvas._standard_output = standard_output_mock  # pylint: disable=protected-access
    illud_state.canvas._terminal_cursor._standard_output = standard_output_mock  # pylint: disable=protected-access
    with patch('illud.terminal.StandardInput'), \
        patch('illud.terminal.StandardOutput', return_value=standard_output_mock), \
        patch('illud.terminal.Terminal.clear_screen'):

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
    (Exception(), True, False, DISABLE_ALTERNATIVE_SCREEN + SHOW_CURSOR),
    (TypeError(), True, False, DISABLE_ALTERNATIVE_SCREEN + SHOW_CURSOR),
    (QuitException(), False, True, DISABLE_ALTERNATIVE_SCREEN + SHOW_CURSOR),
])
# yapf: enable
def test_catch(exception: Exception, expect_reraises: bool, expect_exits: bool,
               expected_output: Optional[str]) -> None:
    """Test illud.illud.Illud.catch."""
    terminal_mock = MagicMock(Terminal, reset_attributes=MagicMock())
    type(terminal_mock)._standard_input = MagicMock(StandardInput)  # pylint: disable=protected-access
    standard_output_mock = MagicMock(StandardOutput)
    type(terminal_mock)._standard_output = standard_output_mock  # pylint: disable=protected-access
    type(terminal_mock).disable_alternative_screen = Terminal.disable_alternative_screen
    type(terminal_mock).show_cursor = Terminal.show_cursor

    with patch('illud.illud.Terminal', return_value=terminal_mock):
        with patch('illud.terminal.Terminal.get_size'):
            illud: Illud = Illud()
        standard_output_mock.write.reset_mock()

    if expect_reraises:
        with pytest.raises(type(exception)):
            illud.catch(exception)
        terminal_mock.reset_attributes.assert_called_once()
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
