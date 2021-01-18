"""A text terminal."""
from illud.ansi.escape_codes.erase import CLEAR_SCREEN
from illud.character import Character
from illud.inputs.standard_input import StandardInput
from illud.outputs.standard_output import StandardOutput
from illud.terminal_cursor import TerminalCursor


class Terminal():
    """A text terminal."""
    def __init__(self) -> None:
        self._standard_input: StandardInput = StandardInput()
        self._standard_output: StandardOutput = StandardOutput()
        self._cursor = TerminalCursor(self._standard_input, self._standard_output)

    def get_character(self) -> Character:
        """Return the next character input from the terminal."""
        character: Character = next(self._standard_input)
        return character

    def clear_screen(self) -> None:
        """Clear the terminal of all characters."""
        self._standard_output.write(CLEAR_SCREEN)
        self._standard_output.flush()
