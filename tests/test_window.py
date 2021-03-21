"""Test illud.window."""
from typing import Any, Iterable, Optional, Type

import pytest
from seligimus.maths.integer_position_2d import IntegerPosition2D
from seligimus.maths.integer_size_2d import IntegerSize2D

from illud.buffer import Buffer
from illud.canvas import Canvas
from illud.exceptions.no_columns_exception import NoColumnsException
from illud.exceptions.no_rows_exception import NoRowsException
from illud.window import Window


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('position, size, buffer_, offset, expected_position, expected_size, expected_buffer, expected_offset', [
    (None, None, None, None, IntegerPosition2D(), IntegerSize2D(0, 0), Buffer(), IntegerPosition2D()),
    (IntegerPosition2D(), IntegerSize2D(0, 0), Buffer(), IntegerPosition2D(), IntegerPosition2D(), IntegerSize2D(0, 0), Buffer(), IntegerPosition2D()),
])
# yapf: enable # pylint: enable=line-too-long
# pylint: disable=too-many-arguments
def test_init(position: Optional[IntegerPosition2D], size: Optional[IntegerSize2D],
              buffer_: Optional[Buffer], offset: Optional[IntegerPosition2D],
              expected_position: IntegerPosition2D, expected_size: IntegerSize2D,
              expected_buffer: Buffer, expected_offset: IntegerPosition2D) -> None:
    """Test illud.window.Window.__init__"""
    window: Window = Window(position, size, buffer_, offset)

    assert window.position == expected_position
    assert window.size == expected_size
    assert window.buffer == expected_buffer
    assert window.offset == expected_offset


# yapf: disable
@pytest.mark.parametrize('window, expected_rows', [
    (Window(), range(0, 0)),
    (Window(size=IntegerSize2D(0, 3)), range(0, 3)),
    (Window(IntegerPosition2D(0, 1)), range(1, 1)),
    (Window(IntegerPosition2D(0, 1), IntegerSize2D(0, 3)), range(1, 4)),
    (Window(IntegerPosition2D(0, 7)), range(7, 7)),
    (Window(IntegerPosition2D(0, 7), IntegerSize2D(0, 3)), range(7, 10)),
])
# yapf: enable
def test_rows(window: Window, expected_rows: Iterable[int]) -> None:
    """Test illud.window.Window.rows"""
    rows: Iterable[int] = window.rows

    assert rows == expected_rows


# yapf: disable
@pytest.mark.parametrize('window, expected_columns', [
    (Window(), range(0, 0)),
    (Window(size=IntegerSize2D(3, 0)), range(0, 3)),
    (Window(IntegerPosition2D(1, 0)), range(1, 1)),
    (Window(IntegerPosition2D(1, 0), IntegerSize2D(3, 0)), range(1, 4)),
    (Window(IntegerPosition2D(7, 0)), range(7, 7)),
    (Window(IntegerPosition2D(7, 0), IntegerSize2D(3, 0)), range(7, 10)),
])
# yapf: enable
def test_columns(window: Window, expected_columns: Iterable[int]) -> None:
    """Test illud.window.Window.columns"""
    columns: Iterable[int] = window.columns

    assert columns == expected_columns


# yapf: disable
@pytest.mark.parametrize('window, expected_left_column, expected_exception', [
    (Window(), None, NoColumnsException),
    (Window(IntegerPosition2D(1, 0)), None, NoColumnsException),
    (Window(IntegerPosition2D(3, 0)), None, NoColumnsException),
    (Window(size=IntegerSize2D(1, 0)), 0, None),
    (Window(IntegerPosition2D(1, 0), IntegerSize2D(1, 0)), 1, None),
    (Window(IntegerPosition2D(3, 0), IntegerSize2D(1, 0)), 3, None),
    (Window(size=IntegerSize2D(3, 0)), 0, None),
    (Window(IntegerPosition2D(1, 0), IntegerSize2D(3, 0)), 1, None),
    (Window(IntegerPosition2D(3, 0), IntegerSize2D(3, 0)), 3, None),
])
# yapf: enable
def test_left_column(window: Window, expected_left_column: Optional[int],
                     expected_exception: Optional[Type[Exception]]) -> None:
    """Test illud.window.Window.left_column."""
    if expected_exception:
        with pytest.raises(expected_exception):
            window.left_column  # pylint: disable=pointless-statement
    else:
        left_column: int = window.left_column

        assert left_column == expected_left_column


# yapf: disable
@pytest.mark.parametrize('window, expected_right_column, expected_exception', [
    (Window(), None, NoColumnsException),
    (Window(IntegerPosition2D(1, 0)), None, NoColumnsException),
    (Window(IntegerPosition2D(3, 0)), None, NoColumnsException),
    (Window(size=IntegerSize2D(1, 0)), 0, None),
    (Window(IntegerPosition2D(1, 0), IntegerSize2D(1, 0)), 1, None),
    (Window(IntegerPosition2D(3, 0), IntegerSize2D(1, 0)), 3, None),
    (Window(size=IntegerSize2D(3, 0)), 2, None),
    (Window(IntegerPosition2D(1, 0), IntegerSize2D(3, 0)), 3, None),
    (Window(IntegerPosition2D(3, 0), IntegerSize2D(3, 0)), 5, None),
])
# yapf: enable
def test_right_column(window: Window, expected_right_column: Optional[int],
                      expected_exception: Optional[Type[Exception]]) -> None:
    """Test illud.window.Window.right_column."""
    if expected_exception:
        with pytest.raises(expected_exception):
            window.right_column  # pylint: disable=pointless-statement
    else:
        right_column: int = window.right_column

        assert right_column == expected_right_column


# yapf: disable
@pytest.mark.parametrize('window, expected_top_row, expected_exception', [
    (Window(), None, NoRowsException),
    (Window(IntegerPosition2D(0, 1)), None, NoRowsException),
    (Window(IntegerPosition2D(0, 3)), None, NoRowsException),
    (Window(size=IntegerSize2D(0, 1)), 0, None),
    (Window(IntegerPosition2D(0, 1), IntegerSize2D(0, 1)), 1, None),
    (Window(IntegerPosition2D(0, 3), IntegerSize2D(0, 1)), 3, None),
    (Window(size=IntegerSize2D(0, 3)), 0, None),
    (Window(IntegerPosition2D(0, 1), IntegerSize2D(0, 3)), 1, None),
    (Window(IntegerPosition2D(0, 3), IntegerSize2D(0, 3)), 3, None),
])
# yapf: enable
def test_top_row(window: Window, expected_top_row: Optional[int],
                 expected_exception: Optional[Type[Exception]]) -> None:
    """Test illud.window.Window.top_row."""
    if expected_exception:
        with pytest.raises(expected_exception):
            window.top_row  # pylint: disable=pointless-statement
    else:
        top_row: int = window.top_row

        assert top_row == expected_top_row


# yapf: disable
@pytest.mark.parametrize('window, expected_bottom_row, expected_exception', [
    (Window(), None, NoRowsException),
    (Window(IntegerPosition2D(0, 1)), None, NoRowsException),
    (Window(IntegerPosition2D(0, 3)), None, NoRowsException),
    (Window(size=IntegerSize2D(0, 1)), 0, None),
    (Window(IntegerPosition2D(0, 1), IntegerSize2D(0, 1)), 1, None),
    (Window(IntegerPosition2D(0, 3), IntegerSize2D(0, 1)), 3, None),
    (Window(size=IntegerSize2D(0, 3)), 2, None),
    (Window(IntegerPosition2D(0, 1), IntegerSize2D(0, 3)), 3, None),
    (Window(IntegerPosition2D(0, 3), IntegerSize2D(0, 3)), 5, None),
])
# yapf: enable
def test_bottom_row(window: Window, expected_bottom_row: Optional[int],
                    expected_exception: Optional[Type[Exception]]) -> None:
    """Test illud.window.Window.bottom_row."""
    if expected_exception:
        with pytest.raises(expected_exception):
            window.bottom_row  # pylint: disable=pointless-statement
    else:
        bottom_row: int = window.bottom_row

        assert bottom_row == expected_bottom_row


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('window, other, expected_equality', [
    (Window(), 'foo', False),
    (Window(buffer_=Buffer('foo')), Window(buffer_=Buffer('bar')), False),
    (Window(size=IntegerSize2D(3, 7), buffer_=Buffer('foo')), Window(buffer_=Buffer('foo')), False),
    (Window(IntegerPosition2D(1, 4), buffer_=Buffer('foo')), Window(buffer_=Buffer('foo')), False),
    (Window(IntegerPosition2D(1, 4), IntegerSize2D(3, 7), Buffer('foo')), Window(IntegerPosition2D(1, 4), IntegerSize2D(3, 7), Buffer('foo')), True),
])
# yapf: enable # pylint: enable=line-too-long
def test_eq(window: Window, other: Any, expected_equality: bool) -> None:
    """Test illud.window.Window.__eq__."""
    equality: bool = window == other

    assert equality == expected_equality


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('window, expected_representation', [
    (Window(), 'Window(position=IntegerPosition2D(), size=IntegerSize2D(0, 0), buffer_=Buffer(), offset=IntegerPosition2D())'),
    (Window(buffer_=Buffer('foo')), 'Window(position=IntegerPosition2D(), size=IntegerSize2D(0, 0), buffer_=Buffer(string=\'foo\'), offset=IntegerPosition2D())'),
])
# yapf: enable # pylint: enable=line-too-long
def test_repr(window: Window, expected_representation: str) -> None:
    """Test illud.window.Window.__repr__."""
    representation: str = repr(window)

    assert representation == expected_representation


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('window, offset, expected_offset_after', [
    (Window(size=IntegerSize2D(4, 3)), IntegerPosition2D(0, 0), IntegerPosition2D(0, 0)),
    (Window(size=IntegerSize2D(4, 3)), IntegerPosition2D(-1, 0), IntegerPosition2D(-1, 0)),
    (Window(size=IntegerSize2D(4, 3), offset=IntegerPosition2D(1, 1)), IntegerPosition2D(-1, 0), IntegerPosition2D(0, 1)),
])
# yapf: enable # pylint: enable=line-too-long
def test_move_view(window: Window, offset: IntegerPosition2D,
                   expected_offset_after: IntegerPosition2D) -> None:
    """Test illud.window.Window.move_view."""
    window.move_view(offset)

    assert window.offset == expected_offset_after


# yapf: disable
@pytest.mark.parametrize('window, expected_window_after', [
    (Window(), Window()),
    (Window(offset=IntegerPosition2D(1, 0)), Window()),
    (Window(offset=IntegerPosition2D(2, 0)), Window(offset=IntegerPosition2D(1, 0))),
])
# yapf: enable
def test_move_view_left(window: Window, expected_window_after: Window) -> None:
    """Test illud.window.Window.move_view_left."""
    window.move_view_left()

    assert window == expected_window_after


# yapf: disable
@pytest.mark.parametrize('window, expected_window_after', [
    (Window(), Window(offset=IntegerPosition2D(1, 0))),
    (Window(offset=IntegerPosition2D(1, 0)), Window(offset=IntegerPosition2D(2, 0))),
    (Window(offset=IntegerPosition2D(2, 0)), Window(offset=IntegerPosition2D(3, 0))),
])
# yapf: enable
def test_move_view_right(window: Window, expected_window_after: Window) -> None:
    """Test illud.window.Window.move_view_right."""
    window.move_view_right()

    assert window == expected_window_after


# yapf: disable
@pytest.mark.parametrize('window, expected_window_after', [
    (Window(), Window()),
    (Window(offset=IntegerPosition2D(0, 1)), Window()),
    (Window(offset=IntegerPosition2D(0, 2)), Window(offset=IntegerPosition2D(0, 1))),
])
# yapf: enable
def test_move_view_up(window: Window, expected_window_after: Window) -> None:
    """Test illud.window.Window.move_view_up."""
    window.move_view_up()

    assert window == expected_window_after


# yapf: disable
@pytest.mark.parametrize('window, expected_window_after', [
    (Window(), Window(offset=IntegerPosition2D(0, 1))),
    (Window(offset=IntegerPosition2D(0, 1)), Window(offset=IntegerPosition2D(0, 2))),
    (Window(offset=IntegerPosition2D(0, 2)), Window(offset=IntegerPosition2D(0, 3))),
])
# yapf: enable
def test_move_view_down(window: Window, expected_window_after: Window) -> None:
    """Test illud.window.Window.move_view_down."""
    window.move_view_down()

    assert window == expected_window_after


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('window, index, expected_window', [
    (Window(size=IntegerSize2D(4, 3)), 0, Window(size=IntegerSize2D(4, 3))),
    (Window(size=IntegerSize2D(4, 3), buffer_=Buffer('foo')), 0, Window(size=IntegerSize2D(4, 3), buffer_=Buffer('foo'))),
    (Window(size=IntegerSize2D(1, 1), buffer_=Buffer('\n')), 1, Window(size=IntegerSize2D(1, 1), buffer_=Buffer('\n'), offset=IntegerPosition2D(0, 1))),
    (Window(size=IntegerSize2D(4, 3), buffer_=Buffer('foo bar')), 4, Window(size=IntegerSize2D(4, 3), buffer_=Buffer('foo bar'), offset=IntegerPosition2D(1, 0))),
    (Window(size=IntegerSize2D(4, 3), buffer_=Buffer('foo bar')), 5, Window(size=IntegerSize2D(4, 3), buffer_=Buffer('foo bar'), offset=IntegerPosition2D(2, 0))),
    (Window(size=IntegerSize2D(4, 3), buffer_=Buffer('foo bar'), offset=IntegerPosition2D(1, 0)), 6, Window(size=IntegerSize2D(4, 3), buffer_=Buffer('foo bar'), offset=IntegerPosition2D(3, 0))),
    (Window(size=IntegerSize2D(4, 3), buffer_=Buffer('foo bar'), offset=IntegerPosition2D(1, 0)), 0, Window(size=IntegerSize2D(4, 3), buffer_=Buffer('foo bar'))),
    (Window(size=IntegerSize2D(4, 3), buffer_=Buffer('foo bar'), offset=IntegerPosition2D(2, 0)), 0, Window(size=IntegerSize2D(4, 3), buffer_=Buffer('foo bar'))),
    (Window(size=IntegerSize2D(3, 2), buffer_=Buffer('foo\nbar\nbaz')), 8, Window(size=IntegerSize2D(3, 2), buffer_=Buffer('foo\nbar\nbaz'), offset=IntegerPosition2D(0, 1))),
    (Window(size=IntegerSize2D(3, 2), buffer_=Buffer('foo\nbar\nbaz'), offset=IntegerPosition2D(0, 1)), 0, Window(size=IntegerSize2D(3, 2), buffer_=Buffer('foo\nbar\nbaz'))),
])
# yapf: enable # pylint: enable=line-too-long
def test_adjust_view_to_include(window: Window, index: int, expected_window: Window) -> None:
    """Test illud.window.Window.adjust_view_to_include."""
    window.adjust_view_to_include(index)

    assert window == expected_window


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('window, canvas, expected_canvas_after', [
    (Window(), Canvas(), Canvas()),
    (Window(size=IntegerSize2D(1, 1)), Canvas(IntegerSize2D(1, 1), [['x']]), Canvas(IntegerSize2D(1, 1), [[' ']])),
    (Window(size=IntegerSize2D(1, 1), buffer_=Buffer('a')), Canvas(IntegerSize2D(1, 1), [['x']]), Canvas(IntegerSize2D(1, 1), [['a']])),
    (Window(size=IntegerSize2D(2, 1), buffer_=Buffer('foo')), Canvas(IntegerSize2D(2, 1), [['x', 'x']]), Canvas(IntegerSize2D(2, 1), [['f', 'o']])),
    (Window(size=IntegerSize2D(3, 1), buffer_=Buffer('foo')), Canvas(IntegerSize2D(3, 1), [['x', 'x', 'x']]), Canvas(IntegerSize2D(3, 1), [['f', 'o', 'o']])),
    (Window(size=IntegerSize2D(2, 1), buffer_=Buffer('foo')), Canvas(IntegerSize2D(3, 1), [['x', 'x', 'x']]), Canvas(IntegerSize2D(3, 1), [['f', 'o', 'x']])),
    (Window(size=IntegerSize2D(3, 1), buffer_=Buffer('foo')), Canvas(IntegerSize2D(4, 1), [['x', 'x', 'x', 'x']]), Canvas(IntegerSize2D(4, 1), [['f', 'o', 'o', 'x']])),
    (Window(size=IntegerSize2D(3, 1), buffer_=Buffer('foo')), Canvas(IntegerSize2D(5, 1), [['x', 'x', 'x', 'x', 'x']]), Canvas(IntegerSize2D(5, 1), [['f', 'o', 'o', 'x', 'x']])),
    (Window(size=IntegerSize2D(5, 1), buffer_=Buffer('foo')), Canvas(IntegerSize2D(5, 1), [['x', 'x', 'x', 'x', 'x']]), Canvas(IntegerSize2D(5, 1), [['f', 'o', 'o', ' ', ' ']])),
    (Window(size=IntegerSize2D(5, 1), buffer_=Buffer('foo\n')), Canvas(IntegerSize2D(5, 1), [['x', 'x', 'x', 'x', 'x']]), Canvas(IntegerSize2D(5, 1), [['f', 'o', 'o', ' ', ' ']])),
    (Window(size=IntegerSize2D(2, 2), buffer_=Buffer('foo')), Canvas(IntegerSize2D(3, 2), [['x', 'x', 'x'], ['x', 'x', 'x']]), Canvas(IntegerSize2D(3, 2), [['f', 'o', 'x'], [' ', ' ', 'x']])),
    (Window(size=IntegerSize2D(1, 2), buffer_=Buffer('f')), Canvas(IntegerSize2D(2, 2), [['x', 'x'], ['x', 'x']]), Canvas(IntegerSize2D(2, 2), [['f', 'x'], [' ', 'x']])),
    (Window(size=IntegerSize2D(1, 2), buffer_=Buffer('f\nb')), Canvas(IntegerSize2D(2, 2), [['x', 'x'], ['x', 'x']]), Canvas(IntegerSize2D(2, 2), [['f', 'x'], ['b', 'x']])),
    (Window(size=IntegerSize2D(1, 2), buffer_=Buffer('foo\nb')), Canvas(IntegerSize2D(2, 2), [['x', 'x'], ['x', 'x']]), Canvas(IntegerSize2D(2, 2), [['f', 'x'], ['b', 'x']])),
    (Window(size=IntegerSize2D(1, 2), buffer_=Buffer('foo\nbar')), Canvas(IntegerSize2D(2, 2), [['x', 'x'], ['x', 'x']]), Canvas(IntegerSize2D(2, 2), [['f', 'x'], ['b', 'x']])),
    (Window(size=IntegerSize2D(2, 2), buffer_=Buffer('f\nb')), Canvas(IntegerSize2D(2, 2), [['x', 'x'], ['x', 'x']]), Canvas(IntegerSize2D(2, 2), [['f', ' '], ['b', ' ']])),
    (Window(size=IntegerSize2D(5, 2), buffer_=Buffer('foo\nbar')), Canvas(IntegerSize2D(5, 2), [['x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x']]), Canvas(IntegerSize2D(5, 2), [['f', 'o', 'o', ' ', ' '], ['b', 'a', 'r', ' ', ' ']])),
    (Window(size=IntegerSize2D(5, 3), buffer_=Buffer('foo\nbar\nbaz')), Canvas(IntegerSize2D(5, 3), [['x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x']]), Canvas(IntegerSize2D(5, 3), [['f', 'o', 'o', ' ', ' '], ['b', 'a', 'r', ' ', ' '], ['b', 'a', 'z', ' ', ' ']])),
    (Window(size=IntegerSize2D(3, 1), buffer_=Buffer('foo'), offset=IntegerPosition2D(1, 0)), Canvas(IntegerSize2D(3, 1), [['x', 'x', 'x']]), Canvas(IntegerSize2D(3, 1), [['o', 'o', ' ']])),
    (Window(size=IntegerSize2D(3, 2), buffer_=Buffer('foo\nbar'), offset=IntegerPosition2D(1, 0)), Canvas(IntegerSize2D(3, 2), [['x', 'x', 'x'], ['x', 'x', 'x']]), Canvas(IntegerSize2D(3, 2), [['o', 'o', ' '], ['a', 'r', ' ']])),
    (Window(size=IntegerSize2D(3, 3), buffer_=Buffer('foo\n\nbar'), offset=IntegerPosition2D(1, 0)), Canvas(IntegerSize2D(3, 3), [['x', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x']]), Canvas(IntegerSize2D(3, 3), [['o', 'o', ' '], [' ', ' ', ' '], ['a', 'r', ' ']])),
    (Window(size=IntegerSize2D(3, 1), buffer_=Buffer('foo'), offset=IntegerPosition2D(-1, 0)), Canvas(IntegerSize2D(3, 1), [['x', 'x', 'x']]), Canvas(IntegerSize2D(3, 1), [[' ', 'f', 'o']])),
    (Window(size=IntegerSize2D(3, 2), buffer_=Buffer('foo\nbar'), offset=IntegerPosition2D(-1, 0)), Canvas(IntegerSize2D(3, 2), [['x', 'x', 'x'], ['x', 'x', 'x']]), Canvas(IntegerSize2D(3, 2), [[' ', 'f', 'o'], [' ', 'b', 'a']])),
    (Window(size=IntegerSize2D(3, 3), buffer_=Buffer('foo\n\nbar'), offset=IntegerPosition2D(-1, 0)), Canvas(IntegerSize2D(3, 3), [['x', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x']]), Canvas(IntegerSize2D(3, 3), [[' ', 'f', 'o'], [' ', ' ', ' '], [' ', 'b', 'a']])),
    (Window(size=IntegerSize2D(3, 1), buffer_=Buffer('foo'), offset=IntegerPosition2D(-4, 0)), Canvas(IntegerSize2D(3, 1), [['x', 'x', 'x']]), Canvas(IntegerSize2D(3, 1), [[' ', ' ', ' ']])),
    (Window(size=IntegerSize2D(3, 2), buffer_=Buffer('foo'), offset=IntegerPosition2D(0, 1)), Canvas(IntegerSize2D(3, 2), [['x', 'x', 'x'], ['x', 'x', 'x']]), Canvas(IntegerSize2D(3, 2), [[' ', ' ', ' '], [' ', ' ', ' ']])),
    (Window(size=IntegerSize2D(3, 2), buffer_=Buffer('foo'), offset=IntegerPosition2D(0, -1)), Canvas(IntegerSize2D(3, 2), [['x', 'x', 'x'], ['x', 'x', 'x']]), Canvas(IntegerSize2D(3, 2), [[' ', ' ', ' '], ['f', 'o', 'o']])),
    (Window(size=IntegerSize2D(3, 2), buffer_=Buffer('foo\nbar'), offset=IntegerPosition2D(0, -1)), Canvas(IntegerSize2D(3, 2), [['x', 'x', 'x'], ['x', 'x', 'x']]), Canvas(IntegerSize2D(3, 2), [[' ', ' ', ' '], ['f', 'o', 'o']])),
    (Window(size=IntegerSize2D(3, 2), buffer_=Buffer('foo'), offset=IntegerPosition2D(0, -2)), Canvas(IntegerSize2D(3, 2), [['x', 'x', 'x'], ['x', 'x', 'x']]), Canvas(IntegerSize2D(3, 2), [[' ', ' ', ' '], [' ', ' ', ' ']])),
])
# yapf: enable # pylint: enable=line-too-long
def test_draw(window: Window, canvas: Canvas, expected_canvas_after: Canvas) -> None:
    """Test illud.window.Window.draw."""
    window.draw(canvas)

    assert canvas == expected_canvas_after
