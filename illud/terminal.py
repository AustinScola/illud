"""A text terminal."""
import os

from seligimus.maths.integer_size_2d import IntegerSize2D

from illud.ansi.escape_codes.cursor import MOVE_CURSOR_HOME
from illud.ansi.escape_codes.erase import CLEAR_SCREEN
from illud.ansi.escape_codes.screen import DISABLE_ALTERNATIVE_SCREEN, ENABLE_ALTERNATIVE_SCREEN
from illud.character import Character
from illud.inputs.standard_input import StandardInput
from illud.outputs.standard_output import StandardOutput
from illud.terminal_cursor import TerminalCursor


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

    def update(self) -> None:
        """Update the terminal contents."""
        self._standard_output.flush()
