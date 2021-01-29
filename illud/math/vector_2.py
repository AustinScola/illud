"""A two-dimensional vector."""
from typing import Any, Generic, TypeVar

T = TypeVar('T', int, float, complex)  # pylint: disable=invalid-name


class Vector2(Generic[T]):
    """A two-dimensional vector."""
    def __init__(self, x: T, y: T):  # pylint: disable=invalid-name
        self.x: T = x  # pylint: disable=invalid-name
        self.y: T = y  # pylint: disable=invalid-name

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Vector2):
            return False

        equality: bool = self.x == other.x and self.y == other.y
        return equality

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(x={self.x}, y={self.y})'

    def __add__(self, other_position: 'Vector2') -> 'Vector2':
        x: T = self.x + other_position.x  # pylint: disable=invalid-name
        y: T = self.y + other_position.y  # pylint: disable=invalid-name
        sum_ = Vector2(x, y)
        return sum_
