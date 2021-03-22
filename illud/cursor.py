"""A position in a string buffer."""
from typing import Any, Optional

from seligimus.maths.integer_position_2d import IntegerPosition2D
from seligimus.python.decorators.operators.equality.equal_instance_attributes import \
    equal_instance_attributes
from seligimus.python.decorators.operators.equality.equal_type import equal_type
from seligimus.python.decorators.standard_representation import standard_representation

from illud.buffer import Buffer
from illud.canvas import Canvas
from illud.characters import WHITESPACE


class Cursor():
    """A position in a string buffer."""
    def __init__(self, buffer_: Optional[Buffer] = None, index: Optional[int] = None):
        self.buffer: Buffer = buffer_ if buffer_ is not None else Buffer()
        self.index: int = index if index is not None else 0

    @equal_type
    @equal_instance_attributes
    def __eq__(self, other: Any) -> bool:
        return True

    @standard_representation(parameter_to_attribute_name={'buffer_': 'buffer'})
    def __repr__(self) -> str:
        pass  # pragma: no cover

    def move_left(self) -> None:
        """Move the cursor left one character."""
        if self.index == 0:
            return

        if self.buffer[self.index - 1] != '\n':
            self.index -= 1

    def move_right(self) -> None:
        """Move the cursor right one character."""
        if not self.buffer:
            return

        if self.index == self.buffer.end:
            return

        if self.buffer[self.index] != '\n':
            self.index += 1

    def move_up(self) -> None:
        """Move the cursor up one line."""
        try:
            line_start: int = self.buffer.reverse_index('\n', end=self.index) + 1
        except ValueError:
            return

        previous_line_start: int
        try:
            previous_line_start = self.buffer.reverse_index('\n', end=line_start - 1) + 1
        except ValueError:
            previous_line_start = 0

        previous_line_length = line_start - previous_line_start
        column: int = self.index - line_start
        if previous_line_length <= column:
            previous_line_end = line_start - 1
            self.index = previous_line_end
        else:
            self.index = previous_line_start + column

    def move_down(self) -> None:
        """Move the cursor down one line."""
        try:
            next_newline_index: int = self.buffer.index('\n', start=self.index)
        except ValueError:
            return

        if next_newline_index == self.buffer.end:
            return

        down_index: int
        column: int = self.buffer.get_column(self.index)
        down_index = next_newline_index + 1 + column

        if down_index > self.buffer.end:
            down_index = self.buffer.end
        else:
            start: int = next_newline_index + 1
            end: int = down_index
            try:
                next_next_newline_index: int = self.buffer.index('\n', start=start, end=end)
                down_index = next_next_newline_index
            except ValueError:
                pass

        self.index = down_index

    def insert(self, string: str) -> None:
        """"Insert a string in the buffer at the current position."""
        self.buffer.insert(string, self.index)
        self.index += len(string)

    def backspace(self) -> None:
        """Remove the character in the position before the cursor."""
        if self.index:
            self.buffer.delete(self.index - 1)
            self.index -= 1

    def delete(self) -> None:
        """Remove the character at the cursor position."""
        if not self.buffer or self.index == len(self.buffer):
            return

        self.buffer.delete(self.index)

        if self.index > self.buffer.end:
            self.index = self.buffer.end

    def next_word(self) -> None:
        """Move the cursor position to the start of the next word."""
        if not self.buffer:
            return

        if self.index == self.buffer.end:
            return

        while True:
            character = self.buffer[self.index]
            if character in WHITESPACE:
                break
            self.index += 1

            if self.index == self.buffer.end:
                return

        while True:
            character = self.buffer[self.index]
            if not character in WHITESPACE:
                break
            self.index += 1

            if self.index == self.buffer.end:
                return

    def move_to_line_start(self) -> None:
        """Move the cursor to the start of the current line."""
        self.index = self.buffer.get_line_start(self.index)

    def move_to_line_end(self) -> None:
        """Move the cursor to the end of the current line."""
        self.index = self.buffer.get_line_end(self.index)

    def draw(self, offset: IntegerPosition2D, canvas: Canvas) -> None:
        """Draw a cursor on the terminal."""
        canvas_position: IntegerPosition2D
        if not self.buffer:
            canvas_position = IntegerPosition2D(0, 0)
        else:
            row: int = self.buffer.get_row(self.index)
            column: int
            if self.index >= len(self.buffer):
                column = self.buffer.get_column(self.index - 1) + 1
            else:
                column = self.buffer.get_column(self.index)
            canvas_position = IntegerPosition2D(column, row)
        canvas_position -= offset

        if not 0 <= canvas_position.x < canvas.size.width:
            return

        if not 0 <= canvas_position.y < canvas.size.height:
            return

        canvas.invert(canvas_position)
