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

    def insert(self, string: str) -> None:
        """"Insert a string in the buffer at the current position."""
        self.buffer.insert(string, self.position)
        self.position += len(string)

    def backspace(self) -> None:
        """Remove the character in the position before the cursor."""
        if self.position:
            self.buffer.delete(self.position - 1)
            self.position -= 1
