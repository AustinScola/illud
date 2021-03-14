"""Test illud.modes.normal."""
from typing import Optional

import pytest

from illud.buffer import Buffer
from illud.character import Character
from illud.characters import CONTROL_C
from illud.cursor import Cursor
from illud.exceptions.quit_exception import QuitException
from illud.illud_state import IlludState
from illud.mode import Mode
from illud.modes.insert import Insert
from illud.modes.normal import Normal


def test_inheritance() -> None:
    """Test illud.modes.normal.Normal inheritance."""
    assert issubclass(Normal, Mode)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('state_before, character, expected_state_after, expect_exits', [
    (IlludState(), Character('i'), IlludState(mode=Insert()), False),
    (IlludState(), Character('d'), IlludState(), False),
    (IlludState(cursor=Cursor(Buffer('foo'), 1)), Character('d'), IlludState(cursor=Cursor(Buffer('foo'), 0)), False),
    (IlludState(), Character('f'), IlludState(), False),
    (IlludState(cursor=Cursor(Buffer('foo'), 0)), Character('f'), IlludState(cursor=Cursor(Buffer('foo'), 1)), False),
    (IlludState(), Character('j'), IlludState(), False),
    (IlludState(Buffer('foo')), Character('k'), IlludState(Buffer('foo')), False),
    (IlludState(cursor=Cursor(Buffer('foo\nbar'), 4)), Character('k'), IlludState(cursor=Cursor(Buffer('foo\nbar'), 0)), False),
    (IlludState(Buffer('foo')), Character('j'), IlludState(Buffer('foo')), False),
    (IlludState(cursor=Cursor(Buffer('foo\nbar'), 0)), Character('j'), IlludState(cursor=Cursor(Buffer('foo\nbar'), 4)), False),
    (IlludState(), Character('k'), IlludState(), False),
    (IlludState(), Character('f'), IlludState(), False),
    (IlludState(), Character('d'), IlludState(), False),
    (IlludState(cursor=Cursor(Buffer('foo'), 0)), Character('x'), IlludState(cursor=Cursor(Buffer('oo'), 0)), False),
    (IlludState(), Character(CONTROL_C), None, True),
])
# yapf: enable # pylint: enable=line-too-long
def test_evaluate(state_before: IlludState, character: Character,
                  expected_state_after: Optional[IlludState], expect_exits: bool) -> None:
    """Test illud.modes.normal.Normal.evaluate."""
    normal: Normal = Normal()

    if expect_exits:
        with pytest.raises(QuitException):
            normal.evaluate(state_before, character)
    else:
        normal.evaluate(state_before, character)

        assert state_before == expected_state_after
