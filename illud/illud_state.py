"""Persistent information of Illud."""
from typing import Any, Optional

from seligimus.maths.integer_position_2d import IntegerPosition2D
from seligimus.maths.integer_size_2d import IntegerSize2D
from seligimus.python.decorators.operators.equality.equal_instance_attributes import \
    equal_instance_attributes
from seligimus.python.decorators.operators.equality.equal_type import equal_type

from illud.buffer import Buffer
from illud.cursor import Cursor
from illud.mode import Mode
from illud.modes.normal import Normal
from illud.state import State
from illud.terminal import Terminal
from illud.window import Window


class IlludState(State):
    """Persistent information of Illud."""

    # pylint: disable=too-many-arguments
    def __init__(self,
                 buffer_: Optional[Buffer] = None,
                 cursor: Optional[Cursor] = None,
                 mode: Optional[Mode] = None,
                 window: Optional[Window] = None,
                 terminal_size: Optional[IntegerSize2D] = None):
        self.buffer: Buffer
        if buffer_ is None:
            self.buffer = Buffer()
        else:
            self.buffer = buffer_

        self.cursor: Cursor
        if cursor is None:
            self.cursor = Cursor(Buffer(), 0)
        else:
            self.cursor = cursor

        self.mode: Mode
        if mode is None:
            self.mode = Normal()
        else:
            self.mode = mode

        self.window: Window
        if window is None:
            self.window = Window(IntegerPosition2D(), IntegerSize2D(0, 0), Buffer())
        else:
            self.window = window

        self.terminal_size: IntegerSize2D
        if terminal_size is None:
            self.terminal_size = IntegerSize2D(0, 0)
        else:
            self.terminal_size = terminal_size

    @staticmethod
    def from_file(file: str) -> 'IlludState':
        """Return Illud state for a file with contents."""
        with open(file) as system_file:
            contents: str = system_file.read()

        terminal_size = Terminal.get_size()
        buffer_: Buffer = Buffer(contents)
        illud_state: IlludState = IlludState(buffer_, terminal_size=terminal_size)

        return illud_state

    @equal_type
    @equal_instance_attributes
    def __eq__(self, other: Any) -> bool:
        return True
