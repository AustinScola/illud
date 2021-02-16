"""Test illud.math.integer_position_2d."""
from seligimus.python.classes.is_subclass_of_generic import is_subclass_of_generic

from illud.math.integer_position_2d import IntegerPosition2D
from illud.math.vector_2 import Vector2


def test_inheritance() -> None:
    """Test illud.math.integer_position_2d.IntegerPosition2D inheritance."""
    assert is_subclass_of_generic(IntegerPosition2D, Vector2[int])
