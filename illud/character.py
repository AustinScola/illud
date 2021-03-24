"""A single string character."""
import string
from typing import Any, Iterator

from seligimus.python.decorators.operators.equality.standard_equality import standard_equality


class Character():
    """A single string character."""
    def __init__(self, value: str):
        self.value: str = value

    @standard_equality
    def __eq__(self, other: Any) -> bool:
        pass  # pragma: no cover

    @property
    def printable(self) -> bool:
        """Return if the character is a printable character or not."""
        return self.value in string.printable


CharacterIterator = Iterator[Character]
