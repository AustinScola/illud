"""Persistent information of Illud."""
from typing import Any

from illud.state import State


class IlludState(State):  # pylint: disable=too-few-public-methods
    """Persistent information of Illud."""
    def __eq__(self, other: Any) -> bool:
        return isinstance(other, IlludState)
