"""Test illud.modes.insert."""
import pytest

from illud.buffer import Buffer
from illud.character import Character
from illud.command import Command
from illud.illud_state import IlludState
from illud.mode import Mode
from illud.modes.insert import Insert


def test_inheritance() -> None:
    """Test illud.modes.insert.Insert inheritance."""
    assert issubclass(Insert, Mode)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('state, command, expected_state_after', [
    (IlludState(mode=Insert()), Command(Character('a')), IlludState(buffer_=Buffer('a'), mode=Insert())),
])
# yapf: enable # pylint: enable=line-too-long
def test_evaluate(state: IlludState, command: Command, expected_state_after: IlludState) -> None:
    """Test illud.modes.insert.Insert.evaluate."""
    Insert.evaluate(state, command)

    assert state == expected_state_after
