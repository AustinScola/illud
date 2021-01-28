"""Test illud.math.integer_position_2d."""
from illud.math.integer_position_2d import IntegerPosition2D
from illud.math.vector_2 import Vector2
from testing.helpers.is_subclass_of_generic import is_subclass_of_generic


def test_inheritance() -> None:
    """Test illud.math.integer_position_2d.IntegerPosition2D inheritance."""
    assert is_subclass_of_generic(IntegerPosition2D, Vector2[int])
