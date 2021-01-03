"""Test illud.illud."""
from typing import Any, Dict, Optional
from unittest.mock import MagicMock, patch

import pytest

from illud.buffer import Buffer
from illud.character import Character
from illud.command import Command
from illud.illud import Illud
from illud.illud_state import IlludState
from illud.repl import REPL


def test_inheritance() -> None:
    """Test illud.illud.Illud inheritance."""
    assert issubclass(Illud, REPL)


# yapf: disable
@pytest.mark.parametrize('illud_initial_state, pass_illud_initial_state, expected_illud_state', [
    (None, False, IlludState()),
    (IlludState(), True, IlludState()),
    (IlludState(Buffer('foo')), True, IlludState(Buffer('foo'))),
])
# yapf: enable
def test_init(illud_initial_state: Optional[IlludState], pass_illud_initial_state: bool,
              expected_illud_state: IlludState) -> None:
    """Test illud.illud.Illud.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_illud_initial_state:
        keyword_arguments['initial_state'] = illud_initial_state

    terminal_mock = MagicMock()
    with patch('illud.illud.Terminal', return_value=terminal_mock):
        illud: Illud = Illud(**keyword_arguments)

        assert illud._terminal == terminal_mock  # pylint: disable=protected-access
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
