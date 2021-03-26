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
        self.buffer: Buffer = buffer_ if buffer_ is not None else Buffer()
        self.cursor: Cursor = cursor if cursor is not None else Cursor()
        self.mode: Mode = mode if mode is not None else Normal()
        self.window: Window = window if window is not None else Window()
        self.canvas: Canvas = canvas if canvas is not None else Canvas()
        self.terminal_size: IntegerSize2D = terminal_size if terminal_size is not None \
            else IntegerSize2D(0, 0)
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
