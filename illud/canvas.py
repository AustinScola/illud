"""A text canvas."""
from itertools import repeat
from typing import Any, List, Optional

from seligimus.maths.integer_position_2d import IntegerPosition2D
from seligimus.maths.integer_size_2d import IntegerSize2D
from seligimus.python.decorators.operators.equality.equal_instance_attributes import \
    equal_instance_attributes
from seligimus.python.decorators.operators.equality.equal_type import equal_type
from seligimus.python.decorators.standard_representation import standard_representation

from illud.ansi.escape_codes.color import INVERT, RESET
from illud.outputs.standard_output import StandardOutput
from illud.terminal_cursor import TerminalCursor

Text = List[List[str]]


class Canvas():
    """A text canvas."""
    def __init__(self,
                 size: Optional[IntegerSize2D] = None,
                 text: Optional[Text] = None,
                 inversions: Optional[List[IntegerPosition2D]] = None):
        self.size: IntegerSize2D = size if size is not None else IntegerSize2D(0, 0)

        self.text: Text
        if text is None:
            self.text = [['' for column in range(self.size.width)]
                         for row in range(self.size.height)]
        else:
            self.text = text

        self._inversions: List[IntegerPosition2D] = inversions if inversions is not None else []
        self._standard_output = StandardOutput()
        self._terminal_cursor = TerminalCursor(self._standard_output)

    @equal_type
    @equal_instance_attributes
    def __eq__(self, other: Any) -> bool:
        return True

    @standard_representation(parameter_to_attribute_name={'inversions': '_inversions'})
    def __repr__(self) -> str:
        pass  # pragma: no cover

    def __getitem__(self, index: int) -> List[str]:
        line: List[str] = self.text[index]
        return line

    def resize(self, size: IntegerSize2D) -> None:
        """Change the size of the canvas."""
        if size.y > self.size.y:
            new_lines = [[' ' for _ in range(size.x)] for _ in range(size.y - self.size.y)]
            self.text.extend(new_lines)
        elif size.y < self.size.y:
            self.text = self.text[:size.y]

        if size.x > self.size.x:
            for line, _ in zip(self.text, range(self.size.y)):
                number_of_new_columns: int = size.x - self.size.x
                new_columns = list(repeat(' ', number_of_new_columns))
                line.extend(new_columns)
        elif size.x < self.size.x:
            for row, line in enumerate(self.text):
                self.text[row] = line[:size.x]

        self.size = size

    def invert(self, position: IntegerPosition2D) -> None:
        """Invert the both the text and background color of a position."""
        if position not in self._inversions:
            self._inversions.append(position)

    def remove_inversions(self) -> None:
        """Remove all inversions."""
        self._inversions = []

    def render(self) -> None:
        """Render the canvas by writing content and control codes to the standard output."""
        for row, line in enumerate(self.text):
            self._terminal_cursor.move(IntegerPosition2D(0, row))
            self._standard_output.write(''.join(line))

        for inversion in self._inversions:
            self._terminal_cursor.move(inversion)
            self._standard_output.write(INVERT)

            character: str = self.text[inversion.y][inversion.x]
            self._standard_output.write(character)

            self._terminal_cursor.move(inversion + IntegerPosition2D(1, 0))
            self._standard_output.write(RESET)
