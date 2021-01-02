"""A string buffer."""
from typing import Any


class Buffer():  # pylint: disable=too-few-public-methods
    """A string buffer."""
    def __init__(self, string: str):
        self.string = string

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Buffer):
            return False

        return self.string == other.string
