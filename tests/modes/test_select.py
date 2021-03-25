"""Test illud.modes.select."""
from typing import Optional

import pytest

from illud.character import Character
from illud.characters import CONTROL_C, ESCAPE
from illud.exceptions.quit_exception import QuitException
from illud.illud_state import IlludState
from illud.mode import Mode
from illud.modes.normal import Normal
from illud.modes.select import Select


def test_inheritance() -> None:
    """Test illud.modes.select.Select inheritance."""
    assert issubclass(Select, Mode)


# yapf: disable
@pytest.mark.parametrize('state, character, expected_state_after, expect_exits', [
    (IlludState(mode=Select()), Character(CONTROL_C), None, True),
    (IlludState(mode=Select()), Character(ESCAPE), IlludState(mode=Normal()), False),
])
# yapf: enable
def test_evaluate(state: IlludState, character: Character,
                  expected_state_after: Optional[IlludState], expect_exits: bool) -> None:
    """Test illud.modes.select.Select.evaluate."""
    if expect_exits:
        with pytest.raises(QuitException):
            Select.evaluate(state, character)
    else:
        Select.evaluate(state, character)

        assert state == expected_state_after
