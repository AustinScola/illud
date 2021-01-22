"""A rectangular view of a string buffer."""
from typing import Iterable

from illud.buffer import Buffer
from illud.exceptions.no_columns_exception import NoColumnsException
from illud.exceptions.no_rows_exception import NoRowsException
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

    @property
    def left_column(self) -> int:
        """Return the integer position of the left most column or raise an error if there are no
        columns."""
        if not self.width:
            raise NoColumnsException

        return self.position.x

    @property
    def right_column(self) -> int:
        """Return the integer position of the right most column or raise an error if there are no
        columns."""
        if not self.width:
            raise NoColumnsException

        return self.position.x + self.width - 1

    @property
    def top_row(self) -> int:
        """Return the integer position of the top most row or raise an error if there are no
        rows."""
        if not self.height:
            raise NoRowsException

        return self.position.y

    @property
    def bottom_row(self) -> int:
        """Return the integer position of the bottom most row or raise an error if there are no
        rows."""
        if not self.height:
            raise NoRowsException

        return self.position.y + self.height - 1
