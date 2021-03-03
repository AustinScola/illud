"""Mode for inserting text."""
from typing import TYPE_CHECKING

from illud.character import Character
from illud.characters import BACKSPACE, CARRIAGE_RETURN, ESCAPE, NEWLINE
from illud.command import Command
from illud.mode import Mode

if TYPE_CHECKING:
    from illud.illud_state import IlludState  # pylint: disable=cyclic-import


class Insert(Mode):  # pylint: disable=too-few-public-methods
    """Mode for inserting text."""
    @staticmethod
    def evaluate(state: 'IlludState', command: Command) -> None:
        """Evaluate the command for the given state."""
        super(Insert, Insert).evaluate(state, command)

        character: Character = command.character
        if character.value == ESCAPE:
            from illud.modes.normal import \
                Normal  # pylint: disable=import-outside-toplevel, cyclic-import
            state.mode = Normal()
        elif character.value == CARRIAGE_RETURN:
            state.cursor.insert(NEWLINE)
        elif character.printable:
            string: str = character.value
            state.cursor.insert(string)
        elif character.value == BACKSPACE:
            state.cursor.backspace()
