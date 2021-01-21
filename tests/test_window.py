"""Test illud.window."""
from typing import Iterable

import pytest

from illud.buffer import Buffer
from illud.integer_position_2d import IntegerPosition2D
from illud.window import Window


# yapf: disable
@pytest.mark.parametrize('position, width, height, buffer_', [
    (IntegerPosition2D(0, 0), 0, 0, Buffer()),
])
# yapf: enable
def test_init(position: IntegerPosition2D, width: int, height: int, buffer_: Buffer) -> None:
    """Test illud.window.Window.__init__"""
    window: Window = Window(position, width, height, buffer_)

    assert window.position == position
    assert window.width == width
    assert window.height == height
    assert window.buffer is buffer_


# yapf: disable
@pytest.mark.parametrize('window, expected_rows', [
    (Window(IntegerPosition2D(0, 0), 0, 0, Buffer('')), range(0, 0)),
    (Window(IntegerPosition2D(0, 0), 0, 3, Buffer('')), range(0, 3)),
    (Window(IntegerPosition2D(0, 1), 0, 0, Buffer('')), range(1, 1)),
    (Window(IntegerPosition2D(0, 1), 0, 3, Buffer('')), range(1, 4)),
    (Window(IntegerPosition2D(0, 7), 0, 0, Buffer('')), range(7, 7)),
    (Window(IntegerPosition2D(0, 7), 0, 3, Buffer('')), range(7, 10)),
])
# yapf: enable
def test_rows(window: Window, expected_rows: Iterable[int]) -> None:
    """Test illud.window.Window.rows"""
    rows: Iterable[int] = window.rows

    assert rows == expected_rows


# yapf: disable
@pytest.mark.parametrize('window, expected_columns', [
    (Window(IntegerPosition2D(0, 0), 0, 0, Buffer('')), range(0, 0)),
    (Window(IntegerPosition2D(0, 0), 3, 0, Buffer('')), range(0, 3)),
    (Window(IntegerPosition2D(1, 0), 0, 0, Buffer('')), range(1, 1)),
    (Window(IntegerPosition2D(1, 0), 3, 0, Buffer('')), range(1, 4)),
    (Window(IntegerPosition2D(7, 0), 0, 0, Buffer('')), range(7, 7)),
    (Window(IntegerPosition2D(7, 0), 3, 0, Buffer('')), range(7, 10)),
])
# yapf: enable
def test_columns(window: Window, expected_columns: Iterable[int]) -> None:
    """Test illud.window.Window.columns"""
    columns: Iterable[int] = window.columns

    assert columns == expected_columns
