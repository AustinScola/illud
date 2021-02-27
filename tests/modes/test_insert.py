"""Test illud.modes.insert."""
import pytest

from illud.buffer import Buffer
from illud.character import Character
from illud.characters import BACKSPACE
from illud.command import Command
from illud.illud_state import IlludState
from illud.mode import Mode
from illud.modes.insert import Insert


def test_inheritance() -> None:
    """Test illud.modes.insert.Insert inheritance."""
    assert issubclass(Insert, Mode)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('state, command, expected_state_after', [
    (IlludState(mode=Insert()), Command(Character('a')), IlludState(buffer_=Buffer('a'), cursor_position=1, mode=Insert())),
    (IlludState(buffer_=Buffer('foo'), mode=Insert()), Command(Character(BACKSPACE)), IlludState(buffer_=Buffer('foo'), mode=Insert())),
    (IlludState(buffer_=Buffer('foo'), cursor_position=2, mode=Insert()), Command(Character('')), IlludState(buffer_=Buffer('fo'), cursor_position=1, mode=Insert())),
])
# yapf: enable # pylint: enable=line-too-long
def test_evaluate(state: IlludState, command: Command, expected_state_after: IlludState) -> None:
    """Test illud.modes.insert.Insert.evaluate."""
    Insert.evaluate(state, command)

    assert state == expected_state_after
