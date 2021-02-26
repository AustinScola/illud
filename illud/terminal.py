"""A text terminal."""
import os
from typing import Iterable, Iterator

from seligimus.maths.integer_position_2d import IntegerPosition2D
from seligimus.maths.integer_size_2d import IntegerSize2D

from illud.ansi.escape_codes.erase import CLEAR_SCREEN
from illud.character import Character
from illud.inputs.standard_input import StandardInput
from illud.outputs.standard_output import StandardOutput
from illud.terminal_cursor import TerminalCursor
from illud.window import Window


class Terminal():
    """A text terminal."""
    def __init__(self) -> None:
        self._standard_input: StandardInput = StandardInput()
        self._standard_output: StandardOutput = StandardOutput()
        self._cursor = TerminalCursor(self._standard_input, self._standard_output)

    @staticmethod
    def get_size() -> IntegerSize2D:
        """Return the size of the terminal."""
        os_terminal_size: os.terminal_size = os.get_terminal_size()
        width: int = os_terminal_size.columns
        height: int = os_terminal_size.lines
        size: IntegerSize2D = IntegerSize2D(width, height)
        return size

    def get_character(self) -> Character:
        """Return the next character input from the terminal."""
        character: Character = next(self._standard_input)
        return character

    def clear_screen(self) -> None:
        """Clear the terminal of all characters."""
        self._standard_output.write(CLEAR_SCREEN)
        self._standard_output.flush()

    def draw_window(self, window: Window) -> None:
        """Draw a window on the terminal."""
        if not window.size.width or not window.size.height:
            return

        buffer_index: int = 0
        rows: Iterable[int] = window.rows
        try:
            for row in rows:
                self._cursor.move(IntegerPosition2D(window.position.x, row))
                columns: Iterator[int] = iter(window.columns)
                for column in columns:
                    character: str = window.buffer[buffer_index]

                    if character == '\n':
                        remaining_columns: int = window.right_column - column + 1
                        self._standard_output.write(' ' * remaining_columns)
                        buffer_index += 1
                        break

                    self._standard_output.write(character)
                    buffer_index += 1
                else:
                    try:
                        buffer_index = window.buffer.index('\n', buffer_index) + 1
                    except ValueError:
                        pass

        except IndexError:
            remaining_columns = window.right_column - column + 1
            self._standard_output.write(' ' * remaining_columns)

            for row in range(row + 1, window.position.y + window.size.height):
                self._cursor.move(IntegerPosition2D(window.position.x, row))
                self._standard_output.write(' ' * window.size.width)

        self._standard_output.flush()
