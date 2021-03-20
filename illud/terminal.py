"""A text terminal."""
import os

from seligimus.maths.integer_position_2d import IntegerPosition2D
from seligimus.maths.integer_size_2d import IntegerSize2D

from illud.ansi.escape_codes.cursor import MOVE_CURSOR_HOME
from illud.ansi.escape_codes.erase import CLEAR_SCREEN
from illud.ansi.escape_codes.screen import DISABLE_ALTERNATIVE_SCREEN, ENABLE_ALTERNATIVE_SCREEN
from illud.canvas import Canvas
from illud.character import Character
from illud.cursor import Cursor
from illud.inputs.standard_input import StandardInput
from illud.outputs.standard_output import StandardOutput
from illud.terminal_cursor import TerminalCursor
from illud.window import Window


class Terminal():
    """A text terminal."""
    def __init__(self) -> None:
        self._standard_input: StandardInput = StandardInput()
        self._standard_output: StandardOutput = StandardOutput()
        self._cursor = TerminalCursor(self._standard_output)
        self._cursor.hide()

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

    def enable_alternative_screen(self) -> None:
        """Enable an alternative terminal screen."""
        self._standard_output.write(ENABLE_ALTERNATIVE_SCREEN)
        self._standard_output.flush()

    def disable_alternative_screen(self) -> None:
        """Enable the alternative terminal screen."""
        self._standard_output.write(DISABLE_ALTERNATIVE_SCREEN)
        self._standard_output.flush()

    def clear_screen(self) -> None:
        """Clear the terminal of all characters."""
        self._standard_output.write(CLEAR_SCREEN)
        self._standard_output.flush()

    def move_cursor_home(self) -> None:
        """Move the terminal cursor to the top left position of the terminal."""
        self._standard_output.write(MOVE_CURSOR_HOME)
        self._standard_output.flush()

    @staticmethod
    def draw_window(window: Window, canvas: Canvas) -> None:  # pylint: disable=too-many-branches, too-many-locals
        """Draw a window on the terminal."""
        if not window.size.width or not window.size.height:
            return

        buffer_index: int = 0

        row_offset: int = window.offset.y
        if row_offset > 0:
            try:
                for _ in range(row_offset):
                    buffer_index = window.buffer.index('\n', buffer_index) + 1
            except ValueError:
                buffer_index = len(window.buffer)
        else:
            for row in range(-row_offset):
                for column in range(window.size.width):
                    canvas[row][column] = ' '

        column_offset: int = window.offset.x
        try:
            starting_row: int = 0 if row_offset > 0 else -row_offset
            ending_row: int = window.bottom_row + 1
            for row in range(starting_row, ending_row):

                if column_offset < 0:
                    spaces: int
                    if -column_offset > window.size.width:
                        spaces = window.size.width
                    else:
                        spaces = -column_offset
                    for beginning_column in range(0, spaces):
                        canvas[row][beginning_column] = ' '
                else:
                    for column in range(column_offset):
                        character: str = window.buffer[buffer_index]
                        if character == '\n':
                            break
                        buffer_index += 1

                starting_column: int = 0 if column_offset > 0 else -column_offset
                ending_column: int = window.right_column + 1
                for column in range(starting_column, ending_column):
                    character = window.buffer[buffer_index]

                    if character == '\n':
                        for remaining_column in range(column, window.right_column + 1):
                            canvas[row][remaining_column] = ' '
                        buffer_index += 1
                        break

                    canvas[row][column] = character

                    buffer_index += 1
                else:
                    try:
                        buffer_index = window.buffer.index('\n', buffer_index) + 1
                    except ValueError:
                        buffer_index = len(window.buffer)
        except IndexError:
            for remaining_column in range(column, window.right_column + 1):
                canvas[row][remaining_column] = ' '

            for row in range(row + 1, window.position.y + window.size.height):
                for column in range(starting_column, ending_column):
                    canvas[row][column] = ' '

    def update(self) -> None:
        """Update the terminal contents."""
        self._standard_output.flush()

    @staticmethod
    def draw_cursor(cursor: Cursor, offset: IntegerPosition2D, canvas: Canvas) -> None:
        """Draw a cursor on the terminal."""
        cursor_position_in_terminal: IntegerPosition2D
        if not cursor.buffer:
            cursor_position_in_terminal = IntegerPosition2D(0, 0)
        else:
            row: int = cursor.buffer.get_row(cursor.index)
            column: int
            if cursor.index >= len(cursor.buffer):
                column = cursor.buffer.get_column(cursor.index - 1) + 1
            else:
                column = cursor.buffer.get_column(cursor.index)
            cursor_position_in_terminal = IntegerPosition2D(column, row)
        cursor_position_in_terminal -= offset

        if not 0 <= cursor_position_in_terminal.x < canvas.size.width:
            return

        if not 0 <= cursor_position_in_terminal.y < canvas.size.height:
            return

        canvas.invert(cursor_position_in_terminal)
