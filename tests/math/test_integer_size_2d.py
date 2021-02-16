"""Test illud.math.integer_size_2d."""
import pytest
from seligimus.python.classes.is_subclass_of_generic import is_subclass_of_generic

from illud.math.integer_size_2d import IntegerSize2D
from illud.math.vector_2 import Vector2


def test_inheritance() -> None:
    """Test illud.math.integer_size_2d.IntegerSize2D inheritance."""
    assert is_subclass_of_generic(IntegerSize2D, Vector2[int])


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

    assert integer_size_2d.x == width
    assert integer_size_2d.y == height


# yapf: disable
@pytest.mark.parametrize('integer_size_2d, width', [
    (IntegerSize2D(0, 0), 0),
    (IntegerSize2D(0, 0), 1),
    (IntegerSize2D(0, 0), 3),
    (IntegerSize2D(1, 0), 3),
])
# yapf: enable
def test_width(integer_size_2d: IntegerSize2D, width: int) -> None:
    """Test illud.math.integer_size_2d.IntegerSize2D.width."""
    integer_size_2d.width = width

    assert integer_size_2d.width == width


# yapf: disable
@pytest.mark.parametrize('integer_size_2d, height', [
    (IntegerSize2D(0, 0), 0),
    (IntegerSize2D(0, 0), 1),
    (IntegerSize2D(0, 0), 3),
    (IntegerSize2D(1, 0), 3),
])
# yapf: enable
def test_height(integer_size_2d: IntegerSize2D, height: int) -> None:
    """Test illud.math.integer_size_2d.IntegerSize2D.height."""
    integer_size_2d.height = height

    assert integer_size_2d.height == height


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
