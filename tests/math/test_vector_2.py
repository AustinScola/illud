"""Test illud.math.vector_2."""
from typing import Any

import pytest

from illud.math.vector_2 import T, Vector2


# yapf: disable
@pytest.mark.parametrize('x, y', [
    (0, 0),
    (1, 0),
    (0, 1),
    (1, 1),
    (7.2, 5.4),
])  # pylint: disable=invalid-name
# yapf: enable
def test_init(x: T, y: T) -> None:
    """Test illud.math.vector_2.Vector2.__init__."""
    vector2 = Vector2(x, y)

    assert vector2.x == x
    assert vector2.y == y


# yapf: disable
@pytest.mark.parametrize('vector2, other, expected_equality', [
    (Vector2(0, 0), 'foo', False),
    (Vector2(0, 0), Vector2(0, 1), False),
    (Vector2(0, 0), Vector2(1, 0), False),
    (Vector2(0, 0), Vector2(1, 1), False),
    (Vector2(0, 0), Vector2(0, 0), True),
    (Vector2(0, 1), Vector2(0, 1), True),
    (Vector2(1, 0), Vector2(1, 0), True),
    (Vector2(1, 1), Vector2(1, 1), True),
    (Vector2(1, 2), Vector2(1, 2.0), True),
    (Vector2(7.0, 1.0), Vector2(7.0, 1.0), True),
])
# yapf: enable
def test_eq(vector2: Vector2, other: Any, expected_equality: bool) -> None:
    """Test illud.math.vector2.Vector2.__eq__."""
    equality: bool = vector2 == other

    assert equality == expected_equality


# yapf: disable
@pytest.mark.parametrize('vector_2, expected_string', [
    (Vector2(0, 0), 'Vector2(x=0, y=0)'),
    (Vector2(0, 1), 'Vector2(x=0, y=1)'),
    (Vector2(1, 0), 'Vector2(x=1, y=0)'),
    (Vector2(1, 1), 'Vector2(x=1, y=1)'),
    (Vector2(7.0, 1.0), 'Vector2(x=7.0, y=1.0)'),
])
# yapf: enable
def test_repr(vector_2: Vector2, expected_string: str) -> None:
    """Test illud.math.vector_2.Vector2.__repr__."""
    string: str = repr(vector_2)

    assert string == expected_string


# yapf: disable
@pytest.mark.parametrize('position, other_position, expected_sum', [
    (Vector2(0, 0), Vector2(0, 0), Vector2(0, 0)),
    (Vector2(0, 0), Vector2(0, 1), Vector2(0, 1)),
    (Vector2(0, 0), Vector2(1, 0), Vector2(1, 0)),
    (Vector2(0, 0), Vector2(1, 1), Vector2(1, 1)),
    (Vector2(0, 1), Vector2(0, 0), Vector2(0, 1)),
    (Vector2(0, 1), Vector2(0, 1), Vector2(0, 2)),
    (Vector2(0, 1), Vector2(1, 0), Vector2(1, 1)),
    (Vector2(0, 1), Vector2(1, 1), Vector2(1, 2)),
    (Vector2(1, 0), Vector2(0, 0), Vector2(1, 0)),
    (Vector2(1, 0), Vector2(0, 1), Vector2(1, 1)),
    (Vector2(1, 0), Vector2(1, 0), Vector2(2, 0)),
    (Vector2(1, 0), Vector2(1, 1), Vector2(2, 1)),
    (Vector2(1, 1), Vector2(0, 0), Vector2(1, 1)),
    (Vector2(1, 1), Vector2(0, 1), Vector2(1, 2)),
    (Vector2(1, 1), Vector2(0, 0), Vector2(1, 1)),
    (Vector2(1, 1), Vector2(0, 1), Vector2(1, 2)),
])
# yapf: enable
def test_add(position: Vector2, other_position: Vector2, expected_sum: Vector2) -> None:
    """Test illud.math.vector_2.Vector2.__add__."""
    sum_ = position + other_position

    assert sum_ == expected_sum
