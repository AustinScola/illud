"""Test illud.math.integer_size_2d."""
from typing import Any

import pytest

from illud.math.integer_size_2d import IntegerSize2D


# yapf: disable
@pytest.mark.parametrize('width, height', [
    (0, 0),
    (1, 0),
    (0, 1),
    (1, 1),
])
# yapf: enable
def test_init(width: int, height: int) -> None:
    """Test illud.math.integer_size_2d.IntegerSize2D.__init__."""
    integer_size_2d = IntegerSize2D(width, height)

    assert integer_size_2d.width == width
    assert integer_size_2d.height == height


# yapf: disable
@pytest.mark.parametrize('integer_size_2d, other, expected_equality', [
    (IntegerSize2D(0, 0), 'foo', False),
    (IntegerSize2D(0, 0), IntegerSize2D(0, 1), False),
    (IntegerSize2D(0, 0), IntegerSize2D(1, 0), False),
    (IntegerSize2D(0, 0), IntegerSize2D(1, 1), False),
    (IntegerSize2D(0, 0), IntegerSize2D(0, 0), True),
    (IntegerSize2D(0, 1), IntegerSize2D(0, 1), True),
    (IntegerSize2D(1, 0), IntegerSize2D(1, 0), True),
    (IntegerSize2D(1, 1), IntegerSize2D(1, 1), True),
])
# yapf: enable
def test_eq(integer_size_2d: IntegerSize2D, other: Any, expected_equality: bool) -> None:
    """Test illud.integer_size_2d.IntegerSize2D.__eq__."""
    equality: bool = integer_size_2d == other

    assert equality == expected_equality


# yapf: disable
@pytest.mark.parametrize('integer_size_2d, expected_string', [
    (IntegerSize2D(0, 0), 'IntegerSize2D(width=0, height=0)'),
    (IntegerSize2D(0, 1), 'IntegerSize2D(width=0, height=1)'),
    (IntegerSize2D(1, 0), 'IntegerSize2D(width=1, height=0)'),
    (IntegerSize2D(1, 1), 'IntegerSize2D(width=1, height=1)'),
])
# yapf: enable
def test_repr(integer_size_2d: IntegerSize2D, expected_string: str) -> None:
    """Test illud.integer_size_2d.IntegerSize2D.__repr__."""
    string: str = repr(integer_size_2d)

    assert string == expected_string


# yapf: disable
@pytest.mark.parametrize('size, other_size, expected_sum', [
    (IntegerSize2D(0, 0), IntegerSize2D(0, 0), IntegerSize2D(0, 0)),
    (IntegerSize2D(0, 0), IntegerSize2D(0, 1), IntegerSize2D(0, 1)),
    (IntegerSize2D(0, 0), IntegerSize2D(1, 0), IntegerSize2D(1, 0)),
    (IntegerSize2D(0, 0), IntegerSize2D(1, 1), IntegerSize2D(1, 1)),
    (IntegerSize2D(0, 1), IntegerSize2D(0, 0), IntegerSize2D(0, 1)),
    (IntegerSize2D(0, 1), IntegerSize2D(0, 1), IntegerSize2D(0, 2)),
    (IntegerSize2D(0, 1), IntegerSize2D(1, 0), IntegerSize2D(1, 1)),
    (IntegerSize2D(0, 1), IntegerSize2D(1, 1), IntegerSize2D(1, 2)),
    (IntegerSize2D(1, 0), IntegerSize2D(0, 0), IntegerSize2D(1, 0)),
    (IntegerSize2D(1, 0), IntegerSize2D(0, 1), IntegerSize2D(1, 1)),
    (IntegerSize2D(1, 0), IntegerSize2D(1, 0), IntegerSize2D(2, 0)),
    (IntegerSize2D(1, 0), IntegerSize2D(1, 1), IntegerSize2D(2, 1)),
    (IntegerSize2D(1, 1), IntegerSize2D(0, 0), IntegerSize2D(1, 1)),
    (IntegerSize2D(1, 1), IntegerSize2D(0, 1), IntegerSize2D(1, 2)),
    (IntegerSize2D(1, 1), IntegerSize2D(0, 0), IntegerSize2D(1, 1)),
    (IntegerSize2D(1, 1), IntegerSize2D(0, 1), IntegerSize2D(1, 2)),
])
# yapf: enable
def test_add(size: IntegerSize2D, other_size: IntegerSize2D, expected_sum: IntegerSize2D) -> None:
    """Test illud.integer_size_2d.IntegerSize2D.__add__."""
    sum_ = size + other_size

    assert sum_ == expected_sum
