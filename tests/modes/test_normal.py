"""Test illud.modes.normal."""
import pytest

from illud.character import Character
from illud.command import Command
from illud.illud_state import IlludState
from illud.mode import Mode
from illud.modes.insert import Insert
from illud.modes.normal import Normal


def test_inheritance() -> None:
    """Test illud.modes.normal.Normal inheritance."""
    assert issubclass(Normal, Mode)


# yapf: disable
@pytest.mark.parametrize('state_before, command, expected_state_after', [
    (IlludState(), Command(Character('i')), IlludState(mode=Insert())),
])
# yapf: enable
def test_evaluate(state_before: IlludState, command: Command,
                  expected_state_after: IlludState) -> None:
    """Test illud.modes.normal.Normal.evaluate."""
    normal: Normal = Normal()

    normal.evaluate(state_before, command)

    assert state_before == expected_state_after
