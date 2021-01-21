"""A rectangular view of a string buffer."""
from typing import Iterable

from illud.buffer import Buffer
from illud.integer_position_2d import IntegerPosition2D


class Window():
    """A rectangular view of a string buffer."""
    def __init__(self, position: IntegerPosition2D, width: int, height: int, buffer_: Buffer):
        self.position: IntegerPosition2D = position
        self.width: int = width
        self.height: int = height
        self.buffer: Buffer = buffer_

    @property
    def rows(self) -> Iterable[int]:
        """Return an iterator of the rows of the window."""
        return range(self.position.y, self.position.y + self.height)

    @property
    def columns(self) -> Iterable[int]:
        """Return an iterator of the columnss of the window."""
        return range(self.position.x, self.position.x + self.width)
