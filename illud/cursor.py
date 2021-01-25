"""A position in a string buffer."""
from typing import Any

from illud.buffer import Buffer


class Cursor():
    """A position in a string buffer."""
    def __init__(self, buffer_: Buffer, position: int):
        self.buffer: Buffer = buffer_
        self.position: int = position

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Cursor):
            return False

        return self.buffer == other.buffer and self.position == other.position

    def __repr__(self) -> str:
        class_name: str = self.__class__.__name__
        buffer_representation: str = repr(self.buffer)
        position_representation: str = str(self.position)

        return f'{class_name}({buffer_representation}, {position_representation})'
