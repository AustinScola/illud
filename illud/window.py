"""A rectangular view of a string buffer."""
from typing import Any, Iterable, Optional

from seligimus.maths.integer_position_2d import IntegerPosition2D
from seligimus.maths.integer_size_2d import IntegerSize2D
from seligimus.python.decorators.operators.equality.equal_instance_attributes import \
    equal_instance_attributes
from seligimus.python.decorators.operators.equality.equal_type import equal_type
from seligimus.python.decorators.standard_representation import standard_representation

from illud.buffer import Buffer
from illud.canvas import Canvas
from illud.exceptions.no_columns_exception import NoColumnsException
from illud.exceptions.no_rows_exception import NoRowsException


class Window():
    """A rectangular view of a string buffer."""
    def __init__(self,
                 position: Optional[IntegerPosition2D] = None,
                 size: Optional[IntegerSize2D] = None,
                 buffer_: Optional[Buffer] = None,
                 offset: Optional[IntegerPosition2D] = None):
        self.position: IntegerPosition2D = position if position is not None else IntegerPosition2D()
        self.size: IntegerSize2D = size if size is not None else IntegerSize2D(0, 0)
        self.buffer: Buffer = buffer_ if buffer_ is not None else Buffer()
        self.offset: IntegerPosition2D = offset if offset is not None else IntegerPosition2D()

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

    @standard_representation(parameter_to_attribute_name={'buffer_': 'buffer'})
    def __repr__(self) -> str:
        pass  # pragma: no cover

    def move_view(self, offset: IntegerPosition2D) -> None:
        """Move the view of the buffer by an offset."""
        self.offset += offset

    def move_view_left(self) -> None:
        """Move the view of the buffer left."""
        if self.offset.x > 0:
            self.offset.x -= 1

    def move_view_right(self) -> None:
        """Move the view of the buffer right."""
        self.offset.x += 1

    def move_view_up(self) -> None:
        """Move the view of the buffer up."""
        if self.offset.y > 0:
            self.offset.y -= 1

    def move_view_down(self) -> None:
        """Move the view of the buffer down."""
        self.offset.y += 1

    def adjust_view_to_include(self, index: int) -> None:
        """Move the view so that it inlcudes an index of the buffer."""
        if not self.buffer:
            return

        position: IntegerPosition2D = self.buffer.get_position(index)
        column: int = position.x
        row: int = position.y

        offset: IntegerPosition2D
        if column > self.offset.x + self.size.width - 1:
            offset = IntegerPosition2D(column - (self.offset.x + self.size.width - 1), 0)
            self.move_view(offset)
        elif column < self.offset.x:
            offset = IntegerPosition2D(column - self.offset.x, 0)
            self.move_view(offset)

        if row > self.offset.y + self.size.height - 1:
            offset = IntegerPosition2D(0, row - (self.offset.y + self.size.height - 1))
            self.move_view(offset)
        if row < self.offset.y:
            offset = IntegerPosition2D(0, row - self.offset.y)
            self.move_view(offset)

    def draw(self, canvas: Canvas) -> None:  # pylint: disable=too-many-branches, too-many-locals
        """Draw a window on the terminal."""
        if not self.size.width or not self.size.height:
            return

        buffer_index: int = 0

        row_offset: int = self.offset.y
        if row_offset > 0:
            try:
                for _ in range(row_offset):
                    buffer_index = self.buffer.index('\n', buffer_index) + 1
            except ValueError:
                buffer_index = len(self.buffer)
        else:
            for row in range(-row_offset):
                for column in range(self.size.width):
                    canvas[row][column] = ' '

        column_offset: int = self.offset.x
        try:
            starting_row: int = 0 if row_offset > 0 else -row_offset
            ending_row: int = self.bottom_row + 1
            for row in range(starting_row, ending_row):

                if column_offset < 0:
                    spaces: int
                    if -column_offset > self.size.width:
                        spaces = self.size.width
                    else:
                        spaces = -column_offset
                    for beginning_column in range(0, spaces):
                        canvas[row][beginning_column] = ' '
                else:
                    for column in range(column_offset):
                        character: str = self.buffer[buffer_index]
                        if character == '\n':
                            break
                        buffer_index += 1

                starting_column: int = 0 if column_offset > 0 else -column_offset
                ending_column: int = self.right_column + 1
                for column in range(starting_column, ending_column):
                    character = self.buffer[buffer_index]

                    if character == '\n':
                        for remaining_column in range(column, self.right_column + 1):
                            canvas[row][remaining_column] = ' '
                        buffer_index += 1
                        break

                    canvas[row][column] = character

                    buffer_index += 1
                else:
                    try:
                        buffer_index = self.buffer.index('\n', buffer_index) + 1
                    except ValueError:
                        buffer_index = len(self.buffer)
        except IndexError:
            for remaining_column in range(column, self.right_column + 1):
                canvas[row][remaining_column] = ' '

            for row in range(row + 1, self.position.y + self.size.height):
                for column in range(starting_column, ending_column):
                    canvas[row][column] = ' '
