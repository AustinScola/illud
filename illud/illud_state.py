"""Persistent information of Illud."""
from typing import Any, Optional

from seligimus.python.decorators.operators.equality.equal_type import equal_type

from illud.buffer import Buffer
from illud.cursor import Cursor
from illud.mode import Mode
from illud.modes.normal import Normal
from illud.state import State


class IlludState(State):  # pylint: disable=too-few-public-methods
    """Persistent information of Illud."""
    def __init__(self,
                 buffer_: Optional[Buffer] = None,
                 cursor_position: Optional[int] = None,
                 mode: Mode = None):
        self.buffer: Buffer
        if buffer_ is None:
            self.buffer = Buffer()
        else:
            self.buffer = buffer_

        self.cursor: Cursor
        if cursor_position is None:
            self.cursor = Cursor(self.buffer, 0)
        else:
            self.cursor = Cursor(self.buffer, cursor_position)

        self.mode: Mode
        if mode is None:
            self.mode = Normal()
        else:
            self.mode = mode

    @equal_type
    def __eq__(self, other: Any) -> bool:
        if self.buffer != other.buffer:
            return False

        if self.mode != other.mode:
            return False

        return True
