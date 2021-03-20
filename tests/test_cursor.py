"""Test illud.cursor."""
from typing import Any

import pytest
from seligimus.maths.integer_position_2d import IntegerPosition2D
from seligimus.maths.integer_size_2d import IntegerSize2D

from illud.buffer import Buffer
from illud.canvas import Canvas
from illud.cursor import Cursor


# yapf: disable
@pytest.mark.parametrize('buffer_,  index', [
    (Buffer(), 0),
    (Buffer('foo'), 1),
])
# yapf: enable
def test_init(buffer_: Buffer, index: int) -> None:
    """Test illud.cursor.Cursor.__init__."""
    cursor: Cursor = Cursor(buffer_, index)

    assert cursor.index == index
    assert cursor.buffer is buffer_


# yapf: disable
@pytest.mark.parametrize('cursor, other, expected_equality', [
    (Cursor(Buffer(), 0), 'foo', False),
    (Cursor(Buffer('foo'), 0), Cursor(Buffer('foo'), 1), False),
    (Cursor(Buffer('foo'), 0), Cursor(Buffer('bar'), 1), False),
    (Cursor(Buffer('foo'), 0), Cursor(Buffer('foo'), 0), True),
])
# yapf: enable
def test_eq(cursor: Cursor, other: Any, expected_equality: bool) -> None:
    """Test illud.cursor.Cursor.__eq__."""
    equality: bool = cursor == other

    assert equality == expected_equality


# yapf: disable
@pytest.mark.parametrize('cursor, expected_representation', [
    (Cursor(Buffer(), 0), 'Cursor(Buffer(), 0)'),
    (Cursor(Buffer('foo'), 0), "Cursor(Buffer(string='foo'), 0)"),
])
# yapf: enable
def test_repr(cursor: Cursor, expected_representation: str) -> None:
    """Test illud.cursor.Cursor.__repr__."""
    representation: str = repr(cursor)

    assert representation == expected_representation


# yapf: disable
@pytest.mark.parametrize('cursor, expected_cursor_after', [
    (Cursor(Buffer(), 0), Cursor(Buffer(), 0)),
    (Cursor(Buffer('foo'), 0), Cursor(Buffer('foo'), 0)),
    (Cursor(Buffer('foo'), 1), Cursor(Buffer('foo'), 0)),
    (Cursor(Buffer('foo'), 2), Cursor(Buffer('foo'), 1)),
    (Cursor(Buffer('foo\nbar'), 3), Cursor(Buffer('foo\nbar'), 2)),
    (Cursor(Buffer('foo\nbar'), 4), Cursor(Buffer('foo\nbar'), 4)),
    (Cursor(Buffer('foo\nbar'), 5), Cursor(Buffer('foo\nbar'), 4)),
    (Cursor(Buffer('foo\nbar'), 6), Cursor(Buffer('foo\nbar'), 5)),
])
# yapf: enable
def test_move_left(cursor: Cursor, expected_cursor_after: Cursor) -> None:
    """Test illud.cursor.Cursor.move_left."""
    cursor.move_left()

    assert cursor == expected_cursor_after


# yapf: disable
@pytest.mark.parametrize('cursor, expected_cursor_after', [
    (Cursor(Buffer(), 0), Cursor(Buffer(), 0)),
    (Cursor(Buffer('foo'), 0), Cursor(Buffer('foo'), 1)),
    (Cursor(Buffer('foo'), 1), Cursor(Buffer('foo'), 2)),
    (Cursor(Buffer('foo'), 2), Cursor(Buffer('foo'), 2)),
    (Cursor(Buffer('foo\nbar'), 3), Cursor(Buffer('foo\nbar'), 3)),
    (Cursor(Buffer('foo\nbar'), 4), Cursor(Buffer('foo\nbar'), 5)),
    (Cursor(Buffer('foo\nbar'), 5), Cursor(Buffer('foo\nbar'), 6)),
    (Cursor(Buffer('foo\nbar'), 6), Cursor(Buffer('foo\nbar'), 6)),
])
# yapf: enable
def test_move_right(cursor: Cursor, expected_cursor_after: Cursor) -> None:
    """Test illud.cursor.Cursor.move_right."""
    cursor.move_right()

    assert cursor == expected_cursor_after


# yapf: disable
@pytest.mark.parametrize('cursor, expected_cursor_after', [
    (Cursor(Buffer(), 0), Cursor(Buffer(), 0)),
    (Cursor(Buffer('foo'), 0), Cursor(Buffer('foo'), 0)),
    (Cursor(Buffer('foo'), 1), Cursor(Buffer('foo'), 1)),
    (Cursor(Buffer('foo\nbar'), 3), Cursor(Buffer('foo\nbar'), 3)),
    (Cursor(Buffer('foo\nbar'), 4), Cursor(Buffer('foo\nbar'), 0)),
    (Cursor(Buffer('foo\nbar'), 5), Cursor(Buffer('foo\nbar'), 1)),
    (Cursor(Buffer('foo\nbar'), 6), Cursor(Buffer('foo\nbar'), 2)),
    (Cursor(Buffer('ham\nspam'), 7), Cursor(Buffer('ham\nspam'), 3)),
    (Cursor(Buffer('ham\nspams'), 8), Cursor(Buffer('ham\nspams'), 3)),
    (Cursor(Buffer('foo\nbar\nbaz'), 8), Cursor(Buffer('foo\nbar\nbaz'), 4)),
    (Cursor(Buffer('foo\nbar\nbaz'), 9), Cursor(Buffer('foo\nbar\nbaz'), 5)),
    (Cursor(Buffer('foo\nbar\nbaz'), 10), Cursor(Buffer('foo\nbar\nbaz'), 6)),
])
# yapf: enable
def test_move_up(cursor: Cursor, expected_cursor_after: Cursor) -> None:
    """Test illud.cursor.Cursor.move_up."""
    cursor.move_up()

    assert cursor == expected_cursor_after


# yapf: disable
@pytest.mark.parametrize('cursor, expected_cursor_after', [
    (Cursor(Buffer(), 0), Cursor(Buffer(), 0)),
    (Cursor(Buffer('foo'), 0), Cursor(Buffer('foo'), 0)),
    (Cursor(Buffer('foo'), 1), Cursor(Buffer('foo'), 1)),
    (Cursor(Buffer('foo\n'), 0), Cursor(Buffer('foo\n'), 0)),
    (Cursor(Buffer('foo\n'), 1), Cursor(Buffer('foo\n'), 1)),
    (Cursor(Buffer('foo\nbar'), 0), Cursor(Buffer('foo\nbar'), 4)),
    (Cursor(Buffer('foo\nbar'), 1), Cursor(Buffer('foo\nbar'), 5)),
    (Cursor(Buffer('wibble\nfoo\nbar',), 5), Cursor(Buffer('wibble\nfoo\nbar'), 10)),
    (Cursor(Buffer('spam\nham'), 3), Cursor(Buffer('spam\nham'), 7)),
    (Cursor(Buffer('spam\nham\neggs'), 3), Cursor(Buffer('spam\nham\neggs'), 8)),
])
# yapf: enable
def test_move_down(cursor: Cursor, expected_cursor_after: Cursor) -> None:
    """Test illud.cursor.Cursor.move_down."""
    cursor.move_down()

    assert cursor == expected_cursor_after


# yapf: disable
@pytest.mark.parametrize('cursor, string, expected_cursor_after', [
    (Cursor(Buffer(), 0), '', Cursor(Buffer(), 0)),
    (Cursor(Buffer(), 0), 'f', Cursor(Buffer('f'), 1)),
    (Cursor(Buffer(), 0), 'foo', Cursor(Buffer('foo'), 3)),
    (Cursor(Buffer('bar'), 0), 'foo', Cursor(Buffer('foobar'), 3)),
    (Cursor(Buffer('foo'), 1), '', Cursor(Buffer('foo'), 1)),
    (Cursor(Buffer('fo'), 1), 'o', Cursor(Buffer('foo'), 2)),
    (Cursor(Buffer('foo'), 3), 'bar', Cursor(Buffer('foobar'), 6)),
])
# yapf: enable
def test_insert(cursor: Cursor, string: str, expected_cursor_after: Cursor) -> None:
    """Test illud.cursor.Cursor.insert."""
    cursor.insert(string)

    assert cursor == expected_cursor_after


# yapf: disable
@pytest.mark.parametrize('cursor, expected_cursor_after', [
    (Cursor(Buffer('foo'), 1), Cursor(Buffer('oo'), 0)),
    (Cursor(Buffer('foo'), 2), Cursor(Buffer('fo'), 1)),
    (Cursor(Buffer('foo'), 3), Cursor(Buffer('fo'), 2)),
])
# yapf: enable
def test_backspace(cursor: Cursor, expected_cursor_after: Cursor) -> None:
    """Test illud.cursor.Cursor.backspace."""
    cursor.backspace()

    assert cursor == expected_cursor_after


# yapf: disable
@pytest.mark.parametrize('cursor, expected_cursor_after', [
    (Cursor(Buffer(), 0), Cursor(Buffer(), 0)),
    (Cursor(Buffer('foo'), 0), Cursor(Buffer('oo'), 0)),
    (Cursor(Buffer('foo'), 1), Cursor(Buffer('fo'), 1)),
    (Cursor(Buffer('foo'), 2), Cursor(Buffer('fo'), 1)),
    (Cursor(Buffer('foo\n'), 3), Cursor(Buffer('foo'), 2)),
])
# yapf: enable
def test_delete(cursor: Cursor, expected_cursor_after: Cursor) -> None:
    """Test illud.cursor.Cursor.delete."""
    cursor.delete()

    assert cursor == expected_cursor_after


# yapf: disable
@pytest.mark.parametrize('cursor, expected_cursor_after', [
    (Cursor(Buffer(), 0), Cursor(Buffer(), 0)),
    (Cursor(Buffer('a b'), 0), Cursor(Buffer('a b'), 2)),
    (Cursor(Buffer('a b'), 1), Cursor(Buffer('a b'), 2)),
    (Cursor(Buffer('a b'), 2), Cursor(Buffer('a b'), 2)),
    (Cursor(Buffer('foo bar'), 1), Cursor(Buffer('foo bar'), 4)),
    (Cursor(Buffer('foo\n\tbar'), 1), Cursor(Buffer('foo\n\tbar'), 5)),
    (Cursor(Buffer('foo bar baz'), 5), Cursor(Buffer('foo bar baz'), 8)),
    (Cursor(Buffer('foo '), 2), Cursor(Buffer('foo '), 3)),
    (Cursor(Buffer('foo  '), 2), Cursor(Buffer('foo  '), 4)),
])
# yapf: enable
def test_next_word(cursor: Cursor, expected_cursor_after: Cursor) -> None:
    """Test illud.cursor.Cursor.next_word."""
    cursor.next_word()

    assert cursor == expected_cursor_after


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('cursor, offset, canvas, expected_canvas_after', [
    (Cursor(Buffer(), 0), IntegerPosition2D(), Canvas(), Canvas()),
    (Cursor(Buffer('foo'), 0), IntegerPosition2D(), Canvas(size=IntegerSize2D(1, 1)), Canvas(size=IntegerSize2D(1, 1), inversions=[IntegerPosition2D()])),
    (Cursor(Buffer('foo'), 1), IntegerPosition2D(), Canvas(size=IntegerSize2D(3, 2)), Canvas(size=IntegerSize2D(3, 2), inversions=[IntegerPosition2D(1, 0)])),
    (Cursor(Buffer('foo'), 2), IntegerPosition2D(), Canvas(size=IntegerSize2D(3, 2)), Canvas(size=IntegerSize2D(3, 2), inversions=[IntegerPosition2D(2, 0)])),
    (Cursor(Buffer('foo\n'), 3), IntegerPosition2D(), Canvas(size=IntegerSize2D(4, 2)), Canvas(size=IntegerSize2D(4, 2), inversions=[IntegerPosition2D(3, 0)])),
    (Cursor(Buffer('foo\nbar'), 3), IntegerPosition2D(), Canvas(size=IntegerSize2D(4, 2)), Canvas(size=IntegerSize2D(4, 2), inversions=[IntegerPosition2D(3, 0)])),
    (Cursor(Buffer('foo\nbar'), 4), IntegerPosition2D(), Canvas(size=IntegerSize2D(4, 2)), Canvas(size=IntegerSize2D(4, 2), inversions=[IntegerPosition2D(0, 1)])),
    (Cursor(Buffer('foo\nbar'), 5), IntegerPosition2D(), Canvas(size=IntegerSize2D(4, 2)), Canvas(size=IntegerSize2D(4, 2), inversions=[IntegerPosition2D(1, 1)])),
    (Cursor(Buffer('foo\nbar'), 6), IntegerPosition2D(), Canvas(size=IntegerSize2D(4, 2)), Canvas(size=IntegerSize2D(4, 2), inversions=[IntegerPosition2D(2, 1)])),
    (Cursor(Buffer('foo\nbar'), 7), IntegerPosition2D(), Canvas(size=IntegerSize2D(4, 2)), Canvas(size=IntegerSize2D(4, 2), inversions=[IntegerPosition2D(3, 1)])),
    (Cursor(Buffer(), 0), IntegerPosition2D(1, 0), Canvas(size=IntegerSize2D(1, 1)), Canvas(size=IntegerSize2D(1, 1))),
    (Cursor(Buffer('foo'), 0), IntegerPosition2D(1, 0), Canvas(size=IntegerSize2D(1, 1)), Canvas(size=IntegerSize2D(1, 1))),
    (Cursor(Buffer('foo'), 0), IntegerPosition2D(2, 0), Canvas(size=IntegerSize2D(1, 1)), Canvas(size=IntegerSize2D(1, 1))),
    (Cursor(Buffer('foo'), 0), IntegerPosition2D(-1, 0), Canvas(size=IntegerSize2D(3, 2)), Canvas(size=IntegerSize2D(3, 2), inversions=[IntegerPosition2D(1, 0)])),
    (Cursor(Buffer('foo'), 0), IntegerPosition2D(0, 1), Canvas(size=IntegerSize2D(1, 1)), Canvas(size=IntegerSize2D(1, 1))),
    (Cursor(Buffer('foo'), 0), IntegerPosition2D(0, -1), Canvas(size=IntegerSize2D(3, 2)), Canvas(size=IntegerSize2D(3, 2), inversions=[IntegerPosition2D(0, 1)])),
    (Cursor(Buffer('foo'), 0), IntegerPosition2D(0, -2), Canvas(size=IntegerSize2D(3, 3)), Canvas(size=IntegerSize2D(3, 3), inversions=[IntegerPosition2D(0, 2)])),
])
# yapf: enable # pylint: enable=line-too-long
def test_draw_cursor(cursor: Cursor, offset: IntegerPosition2D, canvas: Canvas,
                     expected_canvas_after: Canvas) -> None:
    """Test illud.terminal.Terminal.draw_cursor."""
    cursor.draw(offset, canvas)

    assert canvas == expected_canvas_after
