"""A rectangular view of a string buffer."""
from typing import Any, Iterable, Optional

from seligimus.maths.integer_position_2d import IntegerPosition2D
from seligimus.maths.integer_size_2d import IntegerSize2D
from seligimus.python.decorators.operators.equality.standard_equality import standard_equality
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

    @standard_equality
    def __eq__(self, other: Any) -> bool:
        pass  # pragma: no cover

    @standard_representation(parameter_to_attribute_name={'buffer_': 'buffer'})
    def __repr__(self) -> str:
        pass  # pragma: no cover

    def move_view(self, offset: IntegerPosition2D) -> None:
        """Move the view of the buffer by an offset."""
        self.offset -= offset

    def move_view_left(self) -> None:
        """Move the view of the buffer left."""
        if self.offset.x < 0:
            self.offset.x += 1

    def move_view_right(self) -> None:
        """Move the view of the buffer right."""
        self.offset.x -= 1

    def move_view_up(self) -> None:
        """Move the view of the buffer up."""
        if self.offset.y < 0:
            self.offset.y += 1

    def move_view_down(self) -> None:
        """Move the view of the buffer down."""
        self.offset.y -= 1

    def adjust_view_to_include(self, index: int) -> None:
        """Move the view so that it inlcudes an index of the buffer."""
        if not self.buffer:
            return

        position: IntegerPosition2D = self.buffer.get_position(index)
        column: int = position.x
        row: int = position.y

        offset: IntegerPosition2D
        if column > self.size.width - self.offset.x - 1:
            offset = IntegerPosition2D(column - (self.size.width - self.offset.x - 1), 0)
            self.move_view(offset)
        elif column < -self.offset.x:
            offset = IntegerPosition2D(column + self.offset.x, 0)
            self.move_view(offset)

        if row > self.size.height - self.offset.y - 1:
            offset = IntegerPosition2D(0, row - (self.size.height - self.offset.y - 1))
            self.move_view(offset)
        if row < -self.offset.y:
            offset = IntegerPosition2D(0, row + self.offset.y)
            self.move_view(offset)

    def draw(self, canvas: Canvas) -> None:  # pylint: disable=too-many-branches
        """Draw a window on the terminal."""
        if not self.buffer:
            canvas.fill_rectangle(self.position, self.size, ' ')
            return

        canvas.fill_rectangle(self.position, IntegerSize2D(self.size.x, self.offset.y), ' ')

        if self.offset.x > 0:
            fill_position: IntegerPosition2D = IntegerPosition2D(self.position.x,
                                                                 self.position.y + self.offset.y)
            fill_size: IntegerSize2D = IntegerSize2D(min(self.offset.x + 1, self.size.x),
                                                     self.size.y)
            canvas.fill_rectangle(fill_position, fill_size, ' ')

        canvas_row_start = self.position.y if self.offset.y <= 0 \
            else self.position.y + self.offset.y
        canvas_row_end = self.position.y + self.size.y
        canvas_column_start = self.position.x if self.offset.x <= 0 \
            else self.position.x + self.offset.x
        canvas_column_end = self.position.x + self.size.x
        try:
            buffer_index: int = 0

            canvas_row = canvas_row_start
            canvas_column = canvas_column_start

            for _ in range(-self.offset.y):
                while True:
                    character: str = self.buffer[buffer_index]
                    buffer_index += 1
                    if character == '\n':
                        break

            for canvas_row in range(canvas_row_start, canvas_row_end):

                canvas_column = canvas_column_start

                if self.offset.x < 0:
                    for buffer_index in range(buffer_index, buffer_index - self.offset.x + 1):
                        character = self.buffer[buffer_index]
                        if character == '\n':
                            break

                for canvas_column in range(canvas_column_start, canvas_column_end):
                    character = self.buffer[buffer_index]

                    if character == '\n':
                        for canvas_column in range(canvas_column, canvas_column_end):  # pylint: disable=redefined-outer-name
                            canvas[canvas_row][canvas_column] = ' '
                        buffer_index += 1
                        break
                    canvas[canvas_row][canvas_column] = character
                    buffer_index += 1
                else:
                    try:
                        buffer_index = self.buffer.index('\n', buffer_index) + 1
                    except ValueError:
                        buffer_index = len(self.buffer)
        except IndexError:
            for canvas_column in range(canvas_column, canvas_column_end):
                canvas[canvas_row][canvas_column] = ' '

            for canvas_row in range(canvas_row + 1, canvas_row_end):
                for canvas_column in range(canvas_column_start, canvas_column_end):
                    canvas[canvas_row][canvas_column] = ' '
