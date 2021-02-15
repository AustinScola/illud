"""A rectangular view of a string buffer."""
from typing import Any, Iterable

from seligimus.python.decorators.operators.equality.equal_instance_attributes import \
    equal_instance_attributes
from seligimus.python.decorators.operators.equality.equal_type import equal_type

from illud.buffer import Buffer
from illud.exceptions.no_columns_exception import NoColumnsException
from illud.exceptions.no_rows_exception import NoRowsException
from illud.math.integer_position_2d import IntegerPosition2D
from illud.math.integer_size_2d import IntegerSize2D


class Window():
    """A rectangular view of a string buffer."""
    def __init__(self, position: IntegerPosition2D, size: IntegerSize2D, buffer_: Buffer):
        self.position: IntegerPosition2D = position
        self.size: IntegerSize2D = size
        self.buffer: Buffer = buffer_

    @property
    def rows(self) -> Iterable[int]:
        """Return an iterator of the rows of the window."""
        return range(self.position.y, self.position.y + self.size.height)

    @property
    def columns(self) -> Iterable[int]:
        """Return an iterator of the columnss of the window."""
        return range(self.position.x, self.position.x + self.size.width)

    @property
    def left_column(self) -> int:
        """Return the integer position of the left most column or raise an error if there are no
        columns."""
        if not self.size.width:
            raise NoColumnsException

        return self.position.x

    @property
    def right_column(self) -> int:
        """Return the integer position of the right most column or raise an error if there are no
        columns."""
        if not self.size.width:
            raise NoColumnsException

        return self.position.x + self.size.width - 1

    @property
    def top_row(self) -> int:
        """Return the integer position of the top most row or raise an error if there are no
        rows."""
        if not self.size.height:
            raise NoRowsException

        return self.position.y

    @property
    def bottom_row(self) -> int:
        """Return the integer position of the bottom most row or raise an error if there are no
        rows."""
        if not self.size.height:
            raise NoRowsException

        return self.position.y + self.size.height - 1

    @equal_type
    @equal_instance_attributes
    def __eq__(self, other: Any) -> bool:
        return True
