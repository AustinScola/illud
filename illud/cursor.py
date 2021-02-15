"""A position in a string buffer."""
from typing import Any

from seligimus.python.decorators.operators.equality.equal_instance_attributes import \
    equal_instance_attributes
from seligimus.python.decorators.operators.equality.equal_type import equal_type

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

    def __repr__(self) -> str:
        class_name: str = self.__class__.__name__
        buffer_representation: str = repr(self.buffer)
        position_representation: str = str(self.position)

        return f'{class_name}({buffer_representation}, {position_representation})'

    def insert(self, string: str) -> None:
        """"Insert a string in the buffer at the current position."""
        self.buffer.insert(string, self.position)
        self.position += len(string)
