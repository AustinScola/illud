"""A single string character."""
from typing import Any, Iterator


class Character():  # pylint: disable=too-few-public-methods
    """A single string character."""
    def __init__(self, value: str):
        self.value: str = value

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Character):
            return False
        return self.value == other.value


CharacterIterator = Iterator[Character]
