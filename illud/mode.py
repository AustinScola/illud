"""A manner of operation."""
from typing import Any


class Mode():  # pylint: disable=too-few-public-methods
    """A manner of operation."""
    def __eq__(self, other: Any) -> bool:
        return type(self) is type(other)
