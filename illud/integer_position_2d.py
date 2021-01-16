"""A position in the two-dimensional integer lattice."""
from typing import Any


class IntegerPosition2D():
    """A position in the two-dimensional integer lattice."""
    def __init__(self, x: int, y: int):
        self.x: int = x  # pylint: disable=invalid-name
        self.y: int = y  # pylint: disable=invalid-name

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, IntegerPosition2D):
            return False

        return self.x == other.x and self.y == other.y

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(x={self.x}, y={self.y})'

    def __add__(self, other_position: 'IntegerPosition2D') -> 'IntegerPosition2D':
        x: int = self.x + other_position.x  # pylint: disable=invalid-name
        y: int = self.y + other_position.y  # pylint: disable=invalid-name
        sum_ = IntegerPosition2D(x, y)
        return sum_
