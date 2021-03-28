"""A contiguous selection of text."""
from typing import Any, Optional

from seligimus.maths.integer_position_2d import IntegerPosition2D
from seligimus.python.decorators.operators.equality.standard_equality import standard_equality
from seligimus.python.decorators.standard_representation import standard_representation

from illud.buffer import Buffer
from illud.canvas import Canvas
from illud.cursor import Cursor


class Selection():
    """A contiguous selection of text."""
    def __init__(self, buffer_: Optional[Buffer] = None, start: int = 0, end: Optional[int] = None):
        self.buffer: Buffer = buffer_ if buffer_ is not None else Buffer()
        self.start: int = start
        self.end: int = end if end is not None else start

    @staticmethod
    def from_cursor(cursor: Cursor) -> 'Selection':
        """Return a selection from a cursor."""
        selection: Selection = Selection(cursor.buffer, cursor.index)
        return selection

    @property
    def text(self) -> Buffer:
        """Return the text selection."""
        substring: str = self.buffer[self.start:self.end + 1]
        text: Buffer = Buffer(substring)
        return text

    @standard_equality
    def __eq__(self, other: Any) -> bool:
        pass  # pragma: no cover

    @standard_representation(parameter_to_attribute_name={'buffer_': 'buffer'})
    def __repr__(self) -> str:
        pass  # pragma: no cover

    def expand_right(self) -> None:
        """Expand the selection to the right."""
        if not self.buffer:
            return

        if self.end == self.buffer.end:
            return

        if self.buffer[self.end] != '\n':
            self.end += 1

    def draw(self, canvas: Canvas, offset: IntegerPosition2D) -> None:
        """Draw the selection on the canvas."""
        if not self.buffer:
            canvas_position = IntegerPosition2D(0, 0) - offset

            if not 0 <= canvas_position.x < canvas.size.width:
                return

            if not 0 <= canvas_position.y < canvas.size.height:
                return

            canvas.invert(canvas_position)
            return

        for index in range(self.start, self.end + 1):
            row: int = self.buffer.get_row(index)
            column: int
            if index >= len(self.buffer):
                column = self.buffer.get_column(index - 1) + 1
            else:
                column = self.buffer.get_column(index)
            canvas_position = IntegerPosition2D(column, row) - offset

            if not 0 <= canvas_position.x < canvas.size.width:
                continue

            if not 0 <= canvas_position.y < canvas.size.height:
                continue

            canvas.invert(canvas_position)
