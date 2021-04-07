"""A string buffer."""

from typing import Any, Optional, Union

from seligimus.maths.integer_position_2d import IntegerPosition2D
from seligimus.python.decorators.operators.equality.standard_equality import standard_equality
from seligimus.python.decorators.standard_representation import standard_representation

from illud.characters import NEWLINE
from illud.exceptions.buffer_has_no_end_exception import BufferHasNoEndException
from illud.exceptions.buffer_index_exception import BufferIndexException


class Buffer():
    """A string buffer."""
    def __init__(self, string: str = ''):
        self.string: str = string

    @property
    def end(self) -> int:
        """Return the ending index."""
        length: int = len(self)

        if length == 0:
            raise BufferHasNoEndException()

        return length - 1

    @standard_equality
    def __eq__(self, other: Any) -> bool:
        pass  # pragma: no cover

    @standard_representation(parameter_to_attribute_name={'buffer_': 'buffer'})
    def __repr__(self) -> str:
        pass  # pragma: no cover

    def __getitem__(self, index: Union[int, slice]) -> str:
        return self.string.__getitem__(index)

    def __len__(self) -> int:
        return len(self.string)

    def index(self, substring: str, start: Optional[int] = None, end: Optional[int] = None) -> int:
        """Return the lowest index where the substring is found within the range. Raise ValueError
           if the substring is not found."""
        index: int = self.string.index(substring, start, end)
        return index

    def reverse_index(self,
                      substring: str,
                      start: Optional[int] = None,
                      end: Optional[int] = None) -> int:
        """Return the highest index where the substring is found within the range. Raise ValueError
           if the substring is not found."""
        index: int = self.string.rindex(substring, start, end)
        return index

    def get_position(self, index: int) -> IntegerPosition2D:
        """Return the position of an index in the buffer."""
        column: int = self.get_column(index)
        row: int = self.get_row(index)

        position: IntegerPosition2D = IntegerPosition2D(column, row)
        return position

    def get_row(self, index: int) -> int:
        """Return the row number of an index in the buffer."""
        if index > len(self):
            raise BufferIndexException(index, len(self))

        if not self:
            return 0

        row: int = self.string.count('\n', 0, index)

        return row

    def get_column(self, index: int) -> int:
        """Return the column number of an index in the buffer."""
        if not 0 <= index <= len(self):
            raise BufferIndexException(index, len(self))

        column: int = 0
        for character in self[:index][::-1]:
            if character == '\n':
                break
            column += 1

        return column

    def get_line_start(self, index: int) -> int:
        """Return the index of the start of the line which the given index is part of."""
        line_start: int
        try:
            line_start = self.reverse_index(NEWLINE, start=0, end=index) + 1
        except ValueError:
            line_start = 0
        return line_start

    def get_line_end(self, index: int) -> int:
        """Return the index of the end of the line which the given index is part of."""
        line_end: int
        if index >= len(self):
            if not self:
                line_end = 0
            else:
                line_end = len(self)
        else:
            try:
                line_end = self.index(NEWLINE, index, len(self))
            except ValueError:
                line_end = len(self)
        return line_end

    def insert(self, string: str, index: int) -> None:
        """Insert a string at the given index in the buffer."""
        self.string = self.string[:index] + string + self.string[index:]

    def replace(self, index: int, string: str) -> None:
        """Replace the index of the string with another string."""
        if index < 0 or index >= len(self):
            raise BufferIndexException(index, len(self))

        self.string = self.string[:index] + string + self.string[index + 1:]

    def delete(self, index: int) -> None:
        """Delete the character at the given index in the buffer."""
        if not 0 <= index < len(self):
            raise BufferIndexException(index, len(self))

        self.string = self.string[:index] + self.string[index + 1:]

    def delete_row(self, row: int) -> str:
        """Delete the given row of the buffer."""
        line_start: int
        if row:
            newline_index: int = self.index('\n')
            for _ in range(row - 1):
                newline_index = self.index('\n', start=newline_index + 1)
            line_start = newline_index + 1
        else:
            line_start = 0

        line_end: int
        try:
            line_end = self.index('\n', start=line_start)
        except ValueError:
            line_end = len(self)

        line: str = self.string[line_start:line_end + 1]
        self.string = self.string[:line_start] + self.string[line_end + 1:]

        return line
