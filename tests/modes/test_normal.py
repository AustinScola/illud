"""Test illud.modes.normal."""
from typing import Optional

import pytest
from seligimus.maths.integer_position_2d import IntegerPosition2D
from seligimus.maths.integer_size_2d import IntegerSize2D

from illud.buffer import Buffer
from illud.character import Character
from illud.characters import CONTROL_C
from illud.cursor import Cursor
from illud.exceptions.quit_exception import QuitException
from illud.illud_state import IlludState
from illud.mode import Mode
from illud.modes.insert import Insert
from illud.modes.normal import Normal
from illud.modes.replace import Replace
from illud.modes.select import Select
from illud.selection import Selection
from illud.status_bar import StatusBar
from illud.window import Window


def test_name() -> None:
    """Test illud.modes.normal.Normal.name."""
    assert Normal.name == 'Normal'


def test_inheritance() -> None:
    """Test illud.modes.normal.Normal inheritance."""
    assert issubclass(Normal, Mode)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('state_before, character, expected_state_after, expect_exits', [
    (IlludState(), Character('i'), IlludState(mode=Insert(), status_bar=StatusBar(buffer_=Buffer('Insert'))), False),
    (IlludState(), Character('s'), IlludState(mode=Select(), status_bar=StatusBar(buffer_=Buffer('Select')), selection=Selection()), False),
    (IlludState(), Character('r'), IlludState(mode=Replace(), status_bar=StatusBar(buffer_=Buffer('Replace'))), False),
    (IlludState(cursor=Cursor(Buffer('foo'), 1)), Character('s'), IlludState(mode=Select(), cursor=Cursor(Buffer('foo'), 1), status_bar=StatusBar(buffer_=Buffer('Select')), selection=Selection(Buffer('foo'), 1, 1)), False),
    (IlludState(), Character('d'), IlludState(), False),
    (IlludState(cursor=Cursor(Buffer('foo'), 1)), Character('d'), IlludState(cursor=Cursor(Buffer('foo'))), False),
    (IlludState(), Character('f'), IlludState(), False),
    (IlludState(cursor=Cursor(Buffer('foo'), 1), window=Window(size=IntegerSize2D(2, 1), buffer_=Buffer('foo'))), Character('f'), IlludState(cursor=Cursor(Buffer('foo'), 2), window=Window(size=IntegerSize2D(2, 1), buffer_=Buffer('foo'), offset=IntegerPosition2D(-1, 0))), False),
    (IlludState(cursor=Cursor(Buffer('foo'))), Character('f'), IlludState(cursor=Cursor(Buffer('foo'), 1)), False),
    (IlludState(cursor=Cursor(Buffer('foo'), 1), window=Window(size=IntegerSize2D(2, 1), buffer_=Buffer('foo'), offset=IntegerPosition2D(-1, 0))), Character('d'), IlludState(cursor=Cursor(Buffer('foo')), window=Window(size=IntegerSize2D(2, 1), buffer_=Buffer('foo'))), False),
    (IlludState(), Character('j'), IlludState(), False),
    (IlludState(cursor=Cursor(Buffer('foo\nbar\nbaz'), 4), window=Window(size=IntegerSize2D(3, 2), buffer_=Buffer('foo\nbar\nbaz'))), Character('j'), IlludState(cursor=Cursor(Buffer('foo\nbar\nbaz'), 8), window=Window(size=IntegerSize2D(3, 2), buffer_=Buffer('foo\nbar\nbaz'), offset=IntegerPosition2D(0, -1))), False),
    (IlludState(buffer_=Buffer('foo')), Character('k'), IlludState(buffer_=Buffer('foo')), False),
    (IlludState(cursor=Cursor(Buffer('foo\nbar\nbaz'), 4), window=Window(size=IntegerSize2D(3, 2), buffer_=Buffer('foo\nbar\nbaz'), offset=IntegerPosition2D(0, -1))), Character('k'), IlludState(cursor=Cursor(Buffer('foo\nbar\nbaz')), window=Window(size=IntegerSize2D(3, 2), buffer_=Buffer('foo\nbar\nbaz'))), False),
    (IlludState(cursor=Cursor(Buffer('foo\nbar'), 4)), Character('k'), IlludState(cursor=Cursor(Buffer('foo\nbar'))), False),
    (IlludState(buffer_=Buffer('foo')), Character('j'), IlludState(buffer_=Buffer('foo')), False),
    (IlludState(cursor=Cursor(Buffer('foo\nbar'))), Character('j'), IlludState(cursor=Cursor(Buffer('foo\nbar'), 4)), False),
    (IlludState(), Character('k'), IlludState(), False),
    (IlludState(cursor=Cursor(Buffer('foo'), 1), window=Window(size=IntegerSize2D(2, 1), buffer_=Buffer('foo'), offset=IntegerPosition2D(-1, 0))), Character('D'), IlludState(cursor=Cursor(Buffer('foo'), 0), window=Window(size=IntegerSize2D(2, 1), buffer_=Buffer('foo'))), False),
    (IlludState(cursor=Cursor(Buffer('foo'), 0), window=Window(size=IntegerSize2D(2, 1), buffer_=Buffer('foo'))), Character('F'), IlludState(cursor=Cursor(Buffer('foo'), 3), window=Window(size=IntegerSize2D(2, 1), buffer_=Buffer('foo'), offset=IntegerPosition2D(-2, 0))), False),
    (IlludState(cursor=Cursor(Buffer('foo\nbar\nbaz'), 8), window=Window(size=IntegerSize2D(2, 1), buffer_=Buffer('foo\nbar\nbaz'), offset=IntegerPosition2D(0, -2))), Character('K'), IlludState(cursor=Cursor(Buffer('foo\nbar\nbaz')), window=Window(size=IntegerSize2D(2, 1), buffer_=Buffer('foo\nbar\nbaz'))), False),
    (IlludState(cursor=Cursor(Buffer('foo\nbar\nbaz')), window=Window(size=IntegerSize2D(2, 1), buffer_=Buffer('foo\nbar\nbaz'))), Character('J'), IlludState(cursor=Cursor(Buffer('foo\nbar\nbaz'), 8), window=Window(size=IntegerSize2D(2, 1), buffer_=Buffer('foo\nbar\nbaz'), offset=IntegerPosition2D(0, -2))), False),
    (IlludState(cursor=Cursor(Buffer('foo bar'))), Character('w'), IlludState(cursor=Cursor(Buffer('foo bar'), 4)), False),
    (IlludState(cursor=Cursor(Buffer('foo bar')), window=Window(size=IntegerSize2D(2, 1), buffer_=Buffer('foo bar'))), Character('w'), IlludState(cursor=Cursor(Buffer('foo bar'), 4), window=Window(size=IntegerSize2D(2, 1), buffer_=Buffer('foo bar'), offset=IntegerPosition2D(-3, 0))), False),
    (IlludState(cursor=Cursor(Buffer('foo'))), Character('x'), IlludState(cursor=Cursor(Buffer('oo')), clipboard=Buffer('f')), False),
    (IlludState(cursor=Cursor(Buffer('foobaz'), 3), clipboard=Buffer('bar')), Character('p'), IlludState(cursor=Cursor(Buffer('foobarbaz'), 6), clipboard=Buffer('bar')), False),
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
