"""Mode for inserting text."""
from typing import TYPE_CHECKING

from illud.character import Character
from illud.command import Command
from illud.mode import Mode

if TYPE_CHECKING:
    from illud.illud_state import IlludState  # pylint: disable=cyclic-import


class Insert(Mode):  # pylint: disable=too-few-public-methods
    """Mode for inserting text."""
    @staticmethod
    def evaluate(state: 'IlludState', command: Command) -> None:
        """Evaluate the command for the given state."""
        character: Character = command.character
        if character.printable:
            string: str = character.value
            state.cursor.insert(string)
        elif character.value == '':
            state.cursor.backspace()
