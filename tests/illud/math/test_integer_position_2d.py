"""Test illud.math.integer_position_2d."""
from typing import Any

import pytest

from illud.math.integer_position_2d import IntegerPosition2D


# yapf: disable
@pytest.mark.parametrize('x, y', [
    (0, 0),
    (1, 0),
    (0, 1),
    (1, 1),
])  # pylint: disable=invalid-name
# yapf: enable
def test_init(x: int, y: int) -> None:
    """Test illud.math.integer_position_2d.IntegerPosition2D.__init__."""
    integer_position_2d = IntegerPosition2D(x, y)

    assert integer_position_2d.x == x
    assert integer_position_2d.y == y


# yapf: disable
@pytest.mark.parametrize('integer_position_2d, other, expected_equality', [
    (IntegerPosition2D(0, 0), 'foo', False),
    (IntegerPosition2D(0, 0), IntegerPosition2D(0, 1), False),
    (IntegerPosition2D(0, 0), IntegerPosition2D(1, 0), False),
    (IntegerPosition2D(0, 0), IntegerPosition2D(1, 1), False),
    (IntegerPosition2D(0, 0), IntegerPosition2D(0, 0), True),
    (IntegerPosition2D(0, 1), IntegerPosition2D(0, 1), True),
    (IntegerPosition2D(1, 0), IntegerPosition2D(1, 0), True),
    (IntegerPosition2D(1, 1), IntegerPosition2D(1, 1), True),
])
# yapf: enable
def test_eq(integer_position_2d: IntegerPosition2D, other: Any, expected_equality: bool) -> None:
    """Test illud.math.integer_position_2d.IntegerPosition2D.__eq__."""
    equality: bool = integer_position_2d == other

    assert equality == expected_equality


# yapf: disable
@pytest.mark.parametrize('integer_position_2d, expected_string', [
    (IntegerPosition2D(0, 0), 'IntegerPosition2D(x=0, y=0)'),
    (IntegerPosition2D(0, 1), 'IntegerPosition2D(x=0, y=1)'),
    (IntegerPosition2D(1, 0), 'IntegerPosition2D(x=1, y=0)'),
    (IntegerPosition2D(1, 1), 'IntegerPosition2D(x=1, y=1)'),
])
# yapf: enable
def test_repr(integer_position_2d: IntegerPosition2D, expected_string: str) -> None:
    """Test illud.math.integer_position_2d.IntegerPosition2D.__repr__."""
    string: str = repr(integer_position_2d)

    assert string == expected_string


# yapf: disable
@pytest.mark.parametrize('position, other_position, expected_sum', [
    (IntegerPosition2D(0, 0), IntegerPosition2D(0, 0), IntegerPosition2D(0, 0)),
    (IntegerPosition2D(0, 0), IntegerPosition2D(0, 1), IntegerPosition2D(0, 1)),
    (IntegerPosition2D(0, 0), IntegerPosition2D(1, 0), IntegerPosition2D(1, 0)),
    (IntegerPosition2D(0, 0), IntegerPosition2D(1, 1), IntegerPosition2D(1, 1)),
    (IntegerPosition2D(0, 1), IntegerPosition2D(0, 0), IntegerPosition2D(0, 1)),
    (IntegerPosition2D(0, 1), IntegerPosition2D(0, 1), IntegerPosition2D(0, 2)),
    (IntegerPosition2D(0, 1), IntegerPosition2D(1, 0), IntegerPosition2D(1, 1)),
    (IntegerPosition2D(0, 1), IntegerPosition2D(1, 1), IntegerPosition2D(1, 2)),
    (IntegerPosition2D(1, 0), IntegerPosition2D(0, 0), IntegerPosition2D(1, 0)),
    (IntegerPosition2D(1, 0), IntegerPosition2D(0, 1), IntegerPosition2D(1, 1)),
    (IntegerPosition2D(1, 0), IntegerPosition2D(1, 0), IntegerPosition2D(2, 0)),
    (IntegerPosition2D(1, 0), IntegerPosition2D(1, 1), IntegerPosition2D(2, 1)),
    (IntegerPosition2D(1, 1), IntegerPosition2D(0, 0), IntegerPosition2D(1, 1)),
    (IntegerPosition2D(1, 1), IntegerPosition2D(0, 1), IntegerPosition2D(1, 2)),
    (IntegerPosition2D(1, 1), IntegerPosition2D(0, 0), IntegerPosition2D(1, 1)),
    (IntegerPosition2D(1, 1), IntegerPosition2D(0, 1), IntegerPosition2D(1, 2)),
])
# yapf: enable
def test_add(position: IntegerPosition2D, other_position: IntegerPosition2D,
             expected_sum: IntegerPosition2D) -> None:
    """Test illud.math.integer_position_2d.IntegerPosition2D.__add__."""
    sum_ = position + other_position

    assert sum_ == expected_sum
