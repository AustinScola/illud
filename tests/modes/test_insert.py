"""Test illud.modes.insert."""
from typing import Optional

import pytest
from seligimus.maths.integer_position_2d import IntegerPosition2D
from seligimus.maths.integer_size_2d import IntegerSize2D

from illud.buffer import Buffer
from illud.character import Character
from illud.characters import BACKSPACE, CARRIAGE_RETURN, CONTROL_C, ESCAPE
from illud.cursor import Cursor
from illud.exceptions.quit_exception import QuitException
from illud.illud_state import IlludState
from illud.mode import Mode
from illud.modes.insert import Insert
from illud.modes.normal import Normal
from illud.status_bar import StatusBar
from illud.window import Window


def test_name() -> None:
    """Test illud.modes.insert.Insert.name."""
    assert Insert.name == 'Insert'


def test_inheritance() -> None:
    """Test illud.modes.insert.Insert inheritance."""
    assert issubclass(Insert, Mode)


_buffer_0 = Buffer('fo')
_buffer_1 = Buffer()


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('state, character, expected_state_after, expect_exits', [
    (IlludState(mode=Insert()), Character(CONTROL_C), None, True),
    (IlludState(mode=Insert()), Character(ESCAPE), IlludState(mode=Normal(), status_bar=StatusBar(buffer_=Buffer('Normal'))), False),
    (IlludState(mode=Insert()), Character('a'), IlludState(cursor=Cursor(Buffer('a'), 1), mode=Insert()), False),
    (IlludState(cursor=Cursor(_buffer_0, 2), mode=Insert(), window=Window(size=IntegerSize2D(2, 1), buffer_=_buffer_0, offset=IntegerPosition2D(-1, 0))), Character('o'), IlludState(cursor=Cursor(Buffer('foo'), 3), mode=Insert(), window=Window(size=IntegerSize2D(2, 1), buffer_=Buffer('foo'), offset=IntegerPosition2D(-2, 0))), False),
    (IlludState(cursor=Cursor(Buffer('foo')), mode=Insert()), Character(BACKSPACE), IlludState(cursor=Cursor(Buffer('foo')), mode=Insert()), False),
    (IlludState(cursor=Cursor(Buffer('foo'), 2), mode=Insert()), Character(BACKSPACE), IlludState(cursor=Cursor(Buffer('fo'), 1), mode=Insert()), False),
    (IlludState(cursor=Cursor(), mode=Insert()), Character(CARRIAGE_RETURN), IlludState(cursor=Cursor(Buffer('\n'), 1), mode=Insert()), False),
    (IlludState(cursor=Cursor(Buffer('foo'), 2), mode=Insert()), Character(CARRIAGE_RETURN), IlludState(cursor=Cursor(Buffer('fo\no'), 3), mode=Insert()), False),
    (IlludState(mode=Insert(), cursor=Cursor(_buffer_1), window=Window(buffer_=_buffer_1, size=IntegerSize2D(1, 1))), Character(CARRIAGE_RETURN), IlludState(cursor=Cursor(Buffer('\n'), 1), mode=Insert(), window=Window(size=IntegerSize2D(1, 1), buffer_=Buffer('\n'), offset=IntegerPosition2D(0, -1))), False),
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
