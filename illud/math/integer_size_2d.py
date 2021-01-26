"""A size in the two-dimensional integer lattice."""
from typing import Any


class IntegerSize2D():
    """A size in the two-dimensional integer lattice."""
    def __init__(self, width: int, height: int):
        self.width: int = width
        self.height: int = height

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, IntegerSize2D):
            return False

        return self.width == other.width and self.height == other.height

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(width={self.width}, height={self.height})'

    def __add__(self, other_size: 'IntegerSize2D') -> 'IntegerSize2D':
        width: int = self.width + other_size.width
        height: int = self.height + other_size.height
        sum_ = IntegerSize2D(width, height)
        return sum_
