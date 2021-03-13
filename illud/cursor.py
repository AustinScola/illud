"""A position in a string buffer."""
from typing import Any

from seligimus.python.decorators.operators.equality.equal_instance_attributes import \
    equal_instance_attributes
from seligimus.python.decorators.operators.equality.equal_type import equal_type
from seligimus.python.decorators.standard_representation import standard_representation

from illud.buffer import Buffer


class Cursor():
    """A position in a string buffer."""
    def __init__(self, buffer_: Buffer, index: int):
        self.buffer: Buffer = buffer_
        self.index: int = index

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
        if not self.buffer:
            return

        self.buffer.delete(self.index)

        if self.index > self.buffer.end:
            self.index = self.buffer.end
