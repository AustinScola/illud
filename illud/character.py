"""A single string character."""
import string
from typing import Any, Iterator

from seligimus.python.decorators.operators.equality.equal_instance_attributes import \
    equal_instance_attributes
from seligimus.python.decorators.operators.equality.equal_type import equal_type


class Character():
    """A single string character."""
    def __init__(self, value: str):
        self.value: str = value

    @equal_type
    @equal_instance_attributes
    def __eq__(self, other: Any) -> bool:
        return True

    @property
    def printable(self) -> bool:
        """Return if the character is a printable character or not."""
        return self.value in string.printable


CharacterIterator = Iterator[Character]
