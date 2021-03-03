"""A position in a string buffer."""
from typing import Any

from seligimus.python.decorators.operators.equality.equal_instance_attributes import \
    equal_instance_attributes
from seligimus.python.decorators.operators.equality.equal_type import equal_type
from seligimus.python.decorators.standard_representation import standard_representation

from illud.buffer import Buffer


class Cursor():
    """A position in a string buffer."""
    def __init__(self, buffer_: Buffer, position: int):
        self.buffer: Buffer = buffer_
        self.position: int = position

    @equal_type
    @equal_instance_attributes
    def __eq__(self, other: Any) -> bool:
        return True

    @standard_representation(parameter_to_attribute_name={'buffer_': 'buffer'})
    def __repr__(self) -> str:
        pass

    def move_down(self) -> None:
        """Move the cursor down one line."""
        try:
            next_newline_position: int = self.buffer.index('\n', start=self.position)
        except ValueError:
            return

        down_position: int
        column: int = self.buffer.get_column(self.position)
        down_position = next_newline_position + 1 + column

        if down_position > len(self.buffer) - 1:
            down_position = len(self.buffer) - 1
        else:
            start: int = next_newline_position + 1
            end: int = down_position
            try:
                next_next_newline_position: int = self.buffer.index('\n', start=start, end=end)
                down_position = next_next_newline_position
            except ValueError:
                pass

        self.position = down_position

    def insert(self, string: str) -> None:
        """"Insert a string in the buffer at the current position."""
        self.buffer.insert(string, self.position)
        self.position += len(string)

    def backspace(self) -> None:
        """Remove the character in the position before the cursor."""
        if self.position:
            self.buffer.delete(self.position - 1)
            self.position -= 1
