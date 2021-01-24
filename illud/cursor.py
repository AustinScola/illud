"""A position in a string buffer."""
from typing import Any

from illud.buffer import Buffer


class Cursor():  # pylint: disable=too-few-public-methods
    """A position in a string buffer."""
    def __init__(self, buffer_: Buffer, position: int):
        self.buffer: Buffer = buffer_
        self.position: int = position

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Cursor):
            return False

        return self.buffer == other.buffer and self.position == other.position
