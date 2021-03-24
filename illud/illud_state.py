"""Persistent information of Illud."""
from typing import Any, Optional

from seligimus.maths.integer_size_2d import IntegerSize2D
from seligimus.python.decorators.operators.equality.standard_equality import standard_equality

from illud.buffer import Buffer
from illud.canvas import Canvas, Text
from illud.cursor import Cursor
from illud.file import File
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
                 canvas: Optional[Canvas] = None,
                 terminal_size: Optional[IntegerSize2D] = None,
                 file: Optional[File] = None):
        self.buffer: Buffer
        if buffer_ is None:
            self.buffer = Buffer()
        else:
            self.buffer = buffer_

        self.cursor: Cursor
        if cursor is None:
            self.cursor = Cursor()
        else:
            self.cursor = cursor

        self.mode: Mode
        if mode is None:
            self.mode = Normal()
        else:
            self.mode = mode

        self.window: Window
        if window is None:
            self.window = Window()
        else:
            self.window = window

        self.canvas: Canvas
        if canvas is None:
            self.canvas = Canvas()
        else:
            self.canvas = canvas

        self.terminal_size: IntegerSize2D
        if terminal_size is None:
            self.terminal_size = IntegerSize2D(0, 0)
        else:
            self.terminal_size = terminal_size

        self.file: Optional[File] = file

    @staticmethod
    def from_file(path: str) -> 'IlludState':
        """Return Illud state for a file with contents."""
        with open(path) as system_file:
            contents: str = system_file.read()

        buffer_: Buffer = Buffer(contents)
        cursor: Cursor = Cursor(buffer_)
        terminal_size: IntegerSize2D = Terminal.get_size()
        window: Window = Window(size=terminal_size, buffer_=buffer_)
        text: Text = [[' ' for _ in range(terminal_size.width)]
                      for _ in range(terminal_size.height)]
        canvas: Canvas = Canvas(terminal_size, text)
        file: File = File(path)
        illud_state = IlludState(buffer_,
                                 cursor,
                                 window=window,
                                 canvas=canvas,
                                 terminal_size=terminal_size,
                                 file=file)

        return illud_state

    @standard_equality
    def __eq__(self, other: Any) -> bool:
        pass  # pragma: no cover
