"""Test illud.illud."""
from typing import Any, Dict, Optional
from unittest.mock import MagicMock, patch

import pytest
from pytest import CaptureFixture
from seligimus.maths.integer_size_2d import IntegerSize2D

from illud.buffer import Buffer
from illud.character import Character
from illud.command import Command
from illud.illud import Illud
from illud.illud_state import IlludState
from illud.modes.insert import Insert
from illud.repl import REPL


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
        terminal_mock.clear_screen.assert_called_once()

        assert illud._state == expected_illud_state  # pylint: disable=protected-access


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
    (IlludState(terminal_size=IntegerSize2D(1, 1)), None, '\x1b[;H '),
    (IlludState(Buffer('foo'), terminal_size=IntegerSize2D(3, 1)), None, '\x1b[;Hfoo'),
])
# yapf: enable
def test_print(capsys: CaptureFixture, illud_state: IlludState, result: Any,
               expected_output: str) -> None:
    """Test illud.illud.Illud.print."""
    with patch('illud.terminal.StandardInput'), \
        patch('illud.terminal.Terminal.clear_screen'), \
        patch('illud.terminal_cursor.TerminalCursor._get_position_from_terminal'):

        illud: Illud = Illud(illud_state)

    illud.print(result)

    captured_output: str = capsys.readouterr().out
    assert list(captured_output) == list(expected_output)
