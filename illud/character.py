"""A single string character."""
import string
from typing import Any, Iterator


class Character():
    """A single string character."""
    def __init__(self, value: str):
        self.value: str = value

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Character):
            return False
        return self.value == other.value

    @property
    def printable(self) -> bool:
        """Return if the character is a printable character or not."""
        return self.value in string.printable


CharacterIterator = Iterator[Character]
