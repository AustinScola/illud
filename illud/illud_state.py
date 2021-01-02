"""Persistent information of Illud."""
from typing import Any, Optional

from illud.state import State
from illud.buffer import Buffer


class IlludState(State):  # pylint: disable=too-few-public-methods
    """Persistent information of Illud."""
    def __init__(self, buffer_: Optional[Buffer] = None):
        self.buffer: Buffer
        if buffer_ is None:
            self.buffer = Buffer('')
        else:
            self.buffer = buffer_

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, IlludState)
