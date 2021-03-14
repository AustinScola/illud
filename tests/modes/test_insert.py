"""Test illud.modes.insert."""
from typing import Optional

import pytest

from illud.buffer import Buffer
from illud.character import Character
from illud.characters import BACKSPACE, CARRIAGE_RETURN, CONTROL_C, ESCAPE
from illud.cursor import Cursor
from illud.exceptions.quit_exception import QuitException
from illud.illud_state import IlludState
from illud.mode import Mode
from illud.modes.insert import Insert
from illud.modes.normal import Normal


def test_inheritance() -> None:
    """Test illud.modes.insert.Insert inheritance."""
    assert issubclass(Insert, Mode)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('state, character, expected_state_after, expect_exits', [
    (IlludState(mode=Insert()), Character(CONTROL_C), None, True),
    (IlludState(mode=Insert()), Character(ESCAPE), IlludState(mode=Normal()), False),
    (IlludState(mode=Insert()), Character('a'), IlludState(cursor=Cursor(Buffer('a'), 1), mode=Insert()), False),
    (IlludState(cursor=Cursor(Buffer('foo'), 0), mode=Insert()), Character(BACKSPACE), IlludState(cursor=Cursor(Buffer('foo'), 0), mode=Insert()), False),
    (IlludState(cursor=Cursor(Buffer('foo'), 2), mode=Insert()), Character(BACKSPACE), IlludState(cursor=Cursor(Buffer('fo'), 1), mode=Insert()), False),
    (IlludState(cursor=Cursor(Buffer(''), 0), mode=Insert()), Character(CARRIAGE_RETURN), IlludState(cursor=Cursor(Buffer('\n'), 1), mode=Insert()), False),
    (IlludState(cursor=Cursor(Buffer('foo'), 2), mode=Insert()), Character(CARRIAGE_RETURN), IlludState(cursor=Cursor(Buffer('fo\no'), 3), mode=Insert()), False),
])
# yapf: enable # pylint: enable=line-too-long
def test_evaluate(state: IlludState, character: Character,
                  expected_state_after: Optional[IlludState], expect_exits: bool) -> None:
    """Test illud.modes.insert.Insert.evaluate."""
    if expect_exits:
        with pytest.raises(QuitException):
            Insert.evaluate(state, character)
    else:
        Insert.evaluate(state, character)

        assert state == expected_state_after
