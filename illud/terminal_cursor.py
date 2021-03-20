"""The cursor of a terminal."""
from typing import Any

from seligimus.maths.integer_position_2d import IntegerPosition2D
from seligimus.python.decorators.operators.equality.equal_type import equal_type

from illud.ansi.escape_codes.cursor import HIDE_CURSOR, SHOW_CURSOR, get_move_cursor
from illud.outputs.standard_output import StandardOutput


class TerminalCursor():
    """The cursor of a terminal."""
    def __init__(self, standard_output: StandardOutput):
        self._standard_output: StandardOutput = standard_output

    @equal_type
    def __eq__(self, other: Any) -> bool:
        return True

    def hide(self) -> None:
        """Turn off drawing of the terminal cursor."""
        self._standard_output.write(HIDE_CURSOR)

    def show(self) -> None:
        """Turn on drawing of the terminal cursor."""
        self._standard_output.write(SHOW_CURSOR)

    def move(self, position: IntegerPosition2D) -> None:
        """Move the terminal cursor to the position."""
        move_cursor_command = get_move_cursor(position)
        self._standard_output.write(move_cursor_command)
