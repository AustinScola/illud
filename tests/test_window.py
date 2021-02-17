"""Test illud.window."""
from typing import Any, Iterable, Optional, Type

import pytest
from seligimus.maths.integer_position_2d import IntegerPosition2D
from seligimus.maths.integer_size_2d import IntegerSize2D

from illud.buffer import Buffer
from illud.exceptions.no_columns_exception import NoColumnsException
from illud.exceptions.no_rows_exception import NoRowsException
from illud.window import Window


# yapf: disable
@pytest.mark.parametrize('position, size, buffer_', [
    (IntegerPosition2D(0, 0), IntegerSize2D(0, 0), Buffer()),
])
# yapf: enable
def test_init(position: IntegerPosition2D, size: IntegerSize2D, buffer_: Buffer) -> None:
    """Test illud.window.Window.__init__"""
    window: Window = Window(position, size, buffer_)

    assert window.position == position
    assert window.size == size
    assert window.buffer is buffer_


# yapf: disable
@pytest.mark.parametrize('window, expected_rows', [
    (Window(IntegerPosition2D(0, 0), IntegerSize2D(0, 0), Buffer('')), range(0, 0)),
    (Window(IntegerPosition2D(0, 0), IntegerSize2D(0, 3), Buffer('')), range(0, 3)),
    (Window(IntegerPosition2D(0, 1), IntegerSize2D(0, 0), Buffer('')), range(1, 1)),
    (Window(IntegerPosition2D(0, 1), IntegerSize2D(0, 3), Buffer('')), range(1, 4)),
    (Window(IntegerPosition2D(0, 7), IntegerSize2D(0, 0), Buffer('')), range(7, 7)),
    (Window(IntegerPosition2D(0, 7), IntegerSize2D(0, 3), Buffer('')), range(7, 10)),
])
# yapf: enable
def test_rows(window: Window, expected_rows: Iterable[int]) -> None:
    """Test illud.window.Window.rows"""
    rows: Iterable[int] = window.rows

    assert rows == expected_rows


# yapf: disable
@pytest.mark.parametrize('window, expected_columns', [
    (Window(IntegerPosition2D(0, 0), IntegerSize2D(0, 0), Buffer('')), range(0, 0)),
    (Window(IntegerPosition2D(0, 0), IntegerSize2D(3, 0), Buffer('')), range(0, 3)),
    (Window(IntegerPosition2D(1, 0), IntegerSize2D(0, 0), Buffer('')), range(1, 1)),
    (Window(IntegerPosition2D(1, 0), IntegerSize2D(3, 0), Buffer('')), range(1, 4)),
    (Window(IntegerPosition2D(7, 0), IntegerSize2D(0, 0), Buffer('')), range(7, 7)),
    (Window(IntegerPosition2D(7, 0), IntegerSize2D(3, 0), Buffer('')), range(7, 10)),
])
# yapf: enable
def test_columns(window: Window, expected_columns: Iterable[int]) -> None:
    """Test illud.window.Window.columns"""
    columns: Iterable[int] = window.columns

    assert columns == expected_columns


# yapf: disable
@pytest.mark.parametrize('window, expected_left_column, expected_exception', [
    (Window(IntegerPosition2D(0, 0), IntegerSize2D(0, 0), Buffer()), None, NoColumnsException),
    (Window(IntegerPosition2D(1, 0), IntegerSize2D(0, 0), Buffer()), None, NoColumnsException),
    (Window(IntegerPosition2D(3, 0), IntegerSize2D(0, 0), Buffer()), None, NoColumnsException),
    (Window(IntegerPosition2D(0, 0), IntegerSize2D(1, 0), Buffer()), 0, None),
    (Window(IntegerPosition2D(1, 0), IntegerSize2D(1, 0), Buffer()), 1, None),
    (Window(IntegerPosition2D(3, 0), IntegerSize2D(1, 0), Buffer()), 3, None),
    (Window(IntegerPosition2D(0, 0), IntegerSize2D(3, 0), Buffer()), 0, None),
    (Window(IntegerPosition2D(1, 0), IntegerSize2D(3, 0), Buffer()), 1, None),
    (Window(IntegerPosition2D(3, 0), IntegerSize2D(3, 0), Buffer()), 3, None),
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
    (Window(IntegerPosition2D(0, 0), IntegerSize2D(0, 0), Buffer()), None, NoColumnsException),
    (Window(IntegerPosition2D(1, 0), IntegerSize2D(0, 0), Buffer()), None, NoColumnsException),
    (Window(IntegerPosition2D(3, 0), IntegerSize2D(0, 0), Buffer()), None, NoColumnsException),
    (Window(IntegerPosition2D(0, 0), IntegerSize2D(1, 0), Buffer()), 0, None),
    (Window(IntegerPosition2D(1, 0), IntegerSize2D(1, 0), Buffer()), 1, None),
    (Window(IntegerPosition2D(3, 0), IntegerSize2D(1, 0), Buffer()), 3, None),
    (Window(IntegerPosition2D(0, 0), IntegerSize2D(3, 0), Buffer()), 2, None),
    (Window(IntegerPosition2D(1, 0), IntegerSize2D(3, 0), Buffer()), 3, None),
    (Window(IntegerPosition2D(3, 0), IntegerSize2D(3, 0), Buffer()), 5, None),
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
    (Window(IntegerPosition2D(0, 0), IntegerSize2D(0, 0), Buffer()), None, NoRowsException),
    (Window(IntegerPosition2D(0, 1), IntegerSize2D(0, 0), Buffer()), None, NoRowsException),
    (Window(IntegerPosition2D(0, 3), IntegerSize2D(0, 0), Buffer()), None, NoRowsException),
    (Window(IntegerPosition2D(0, 0), IntegerSize2D(0, 1), Buffer()), 0, None),
    (Window(IntegerPosition2D(0, 1), IntegerSize2D(0, 1), Buffer()), 1, None),
    (Window(IntegerPosition2D(0, 3), IntegerSize2D(0, 1), Buffer()), 3, None),
    (Window(IntegerPosition2D(0, 0), IntegerSize2D(0, 3), Buffer()), 0, None),
    (Window(IntegerPosition2D(0, 1), IntegerSize2D(0, 3), Buffer()), 1, None),
    (Window(IntegerPosition2D(0, 3), IntegerSize2D(0, 3), Buffer()), 3, None),
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
    (Window(IntegerPosition2D(0, 0), IntegerSize2D(0, 0), Buffer()), None, NoRowsException),
    (Window(IntegerPosition2D(0, 1), IntegerSize2D(0, 0), Buffer()), None, NoRowsException),
    (Window(IntegerPosition2D(0, 3), IntegerSize2D(0, 0), Buffer()), None, NoRowsException),
    (Window(IntegerPosition2D(0, 0), IntegerSize2D(0, 1), Buffer()), 0, None),
    (Window(IntegerPosition2D(0, 1), IntegerSize2D(0, 1), Buffer()), 1, None),
    (Window(IntegerPosition2D(0, 3), IntegerSize2D(0, 1), Buffer()), 3, None),
    (Window(IntegerPosition2D(0, 0), IntegerSize2D(0, 3), Buffer()), 2, None),
    (Window(IntegerPosition2D(0, 1), IntegerSize2D(0, 3), Buffer()), 3, None),
    (Window(IntegerPosition2D(0, 3), IntegerSize2D(0, 3), Buffer()), 5, None),
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
    (Window(IntegerPosition2D(0, 0), IntegerSize2D(0, 0), Buffer()), 'foo', False),
    (Window(IntegerPosition2D(0, 0), IntegerSize2D(0, 0), Buffer('foo')), Window(IntegerPosition2D(0, 0), IntegerSize2D(0, 0), Buffer('bar')), False),
    (Window(IntegerPosition2D(0, 0), IntegerSize2D(3, 7), Buffer('foo')), Window(IntegerPosition2D(0, 0), IntegerSize2D(0, 0), Buffer('foo')), False),
    (Window(IntegerPosition2D(1, 4), IntegerSize2D(0, 0), Buffer('foo')), Window(IntegerPosition2D(0, 0), IntegerSize2D(0, 0), Buffer('foo')), False),
    (Window(IntegerPosition2D(1, 4), IntegerSize2D(3, 7), Buffer('foo')), Window(IntegerPosition2D(1, 4), IntegerSize2D(3, 7), Buffer('foo')), True),
])
# yapf: enable # pylint: enable=line-too-long
def test_eq(window: Window, other: Any, expected_equality: bool) -> None:
    """Test illud.window.Window.__eq__."""
    equality: bool = window == other

    assert equality == expected_equality
