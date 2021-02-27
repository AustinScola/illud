"""A string buffer."""
from typing import Any, Optional, Union

from seligimus.python.decorators.operators.equality.equal_instance_attributes import \
    equal_instance_attributes
from seligimus.python.decorators.operators.equality.equal_type import equal_type
from seligimus.python.decorators.standard_representation import standard_representation

from illud.exceptions.buffer_position_exception import BufferPositionException


class Buffer():
    """A string buffer."""
    def __init__(self, string: str = ''):
        self.string: str = string

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

    def insert(self, string: str, position: int) -> None:
        """Insert a string at the given position in the buffer."""
        self.string = self.string[:position] + string + self.string[position:]

    def delete(self, position: int) -> None:
        """Delete the character at the given position in the buffer."""
        if not 0 <= position < len(self):
            raise BufferPositionException(position, len(self))

        self.string = self.string[:position] + self.string[position + 1:]
