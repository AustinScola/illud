"""A text terminal."""
from illud.character import Character
from illud.inputs.standard_input import StandardInput


class Terminal():  # pylint: disable=too-few-public-methods
    """A text terminal."""
    def __init__(self) -> None:
        self._standard_input: StandardInput = StandardInput()

    def get_character(self) -> Character:
        """Return the next character input from the terminal."""
        character: Character = next(self._standard_input)
        return character
