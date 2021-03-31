"""Persistent information of Illud."""
from typing import Any, Optional

from seligimus.maths.integer_size_2d import IntegerSize2D
from seligimus.python.decorators.operators.equality.standard_equality import standard_equality
from seligimus.python.decorators.standard_representation import standard_representation

from illud.buffer import Buffer
from illud.canvas import Canvas
from illud.cursor import Cursor
from illud.file import File
from illud.mode import Mode
from illud.modes.normal import Normal
from illud.selection import Selection
from illud.state import State
from illud.status_bar import StatusBar
from illud.terminal import Terminal
from illud.window import Window


class IlludState(State):
    """Persistent information of Illud."""

    # pylint: disable=too-many-arguments, too-many-instance-attributes
    def __init__(self,
                 terminal_size: Optional[IntegerSize2D] = None,
                 buffer_: Optional[Buffer] = None,
                 cursor: Optional[Cursor] = None,
                 selection: Optional[Selection] = None,
                 clipboard: Optional[Buffer] = None,
                 mode: Optional[Mode] = None,
                 window: Optional[Window] = None,
                 status_bar: Optional[StatusBar] = None,
                 canvas: Optional[Canvas] = None,
                 file: Optional[File] = None):
        self.terminal_size: IntegerSize2D = terminal_size if terminal_size is not None \
            else IntegerSize2D(0, 0)
        self.buffer: Buffer = buffer_ if buffer_ is not None else Buffer()
        self.cursor: Cursor = cursor if cursor is not None else Cursor()
        self.selection: Optional[Selection] = selection
        self.clipboard: Optional[Buffer] = clipboard
        self.mode: Mode = mode if mode is not None else Normal()
        self.window: Window = window if window is not None else Window()
        self.status_bar: StatusBar = status_bar if status_bar is not None else StatusBar()
        self.canvas: Canvas = canvas if canvas is not None else Canvas()
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
        canvas: Canvas = Canvas(terminal_size).fill(' ')
        file: File = File(path)
        illud_state = IlludState(terminal_size=terminal_size,
                                 buffer_=buffer_,
                                 cursor=cursor,
                                 window=window,
                                 canvas=canvas,
                                 file=file)

        return illud_state

    @standard_equality
    def __eq__(self, other: Any) -> bool:
        pass  # pragma: no cover

    @standard_representation(parameter_to_attribute_name={'buffer_': 'buffer'})
    def __repr__(self) -> str:
        pass  # pragma: no cover
