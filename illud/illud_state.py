"""Persistent information of Illud."""
from typing import Any, Optional

from illud.buffer import Buffer
from illud.mode import Mode
from illud.modes.normal import Normal
from illud.state import State


class IlludState(State):  # pylint: disable=too-few-public-methods
    """Persistent information of Illud."""
    def __init__(self, buffer_: Optional[Buffer] = None, mode: Mode = None):
        self.buffer: Buffer
        if buffer_ is None:
            self.buffer = Buffer()
        else:
            self.buffer = buffer_

        self.mode: Mode
        if mode is None:
            self.mode = Normal()
        else:
            self.mode = mode

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, IlludState):
            return False

        if self.buffer != other.buffer:
            return False

        if self.mode != other.mode:
            return False

        return True
