"""A string buffer."""
from typing import Any, Optional, Union

from seligimus.python.decorators.operators.equality.equal_instance_attributes import \
    equal_instance_attributes
from seligimus.python.decorators.operators.equality.equal_type import equal_type
from seligimus.python.decorators.standard_representation import standard_representation

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

    @equal_type
    @equal_instance_attributes
    def __eq__(self, other: Any) -> bool:
        return True

    @standard_representation(parameter_to_attribute_name={'buffer_': 'buffer'})
    def __repr__(self) -> str:
        pass

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
        if not 0 <= index < len(self):
            raise BufferIndexException(index, len(self))

        column: int = 0
        if self[index] == '\n' and index == 0:
            pass
        else:
            for character in self[:index][::-1]:
                if character == '\n':
                    break
                column += 1

        return column

    def insert(self, string: str, index: int) -> None:
        """Insert a string at the given index in the buffer."""
        self.string = self.string[:index] + string + self.string[index:]

    def delete(self, index: int) -> None:
        """Delete the character at the given index in the buffer."""
        if not 0 <= index < len(self):
            raise BufferIndexException(index, len(self))

        self.string = self.string[:index] + self.string[index + 1:]
