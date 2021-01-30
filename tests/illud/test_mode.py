"""Test illud.mode."""
from typing import Any

import pytest

from illud.character import Character
from illud.command import Command
from illud.illud_state import IlludState
from illud.mode import Mode


# yapf: disable
@pytest.mark.parametrize('mode, other, expected_equality', [
    (Mode(), 'foo', False),
    (Mode(), 1, False),
    (Mode(), Mode(), True),
])
# yapf: enable
def test_eq(mode: Mode, other: Any, expected_equality: bool) -> None:
    """Test illud.mode.__eq__."""
    equality: bool = mode == other

    assert equality == expected_equality


# yapf: disable
@pytest.mark.parametrize('state_before, command, expected_state_after', [
    (IlludState(), Command(Character('i')), IlludState()),
])
# yapf: enable
def test_evaluate(state_before: IlludState, command: Command,
                  expected_state_after: IlludState) -> None:
    """Test illud.mode.evaluate."""
    mode: Mode = Mode()

    mode.evaluate(state_before, command)

    assert state_before == expected_state_after