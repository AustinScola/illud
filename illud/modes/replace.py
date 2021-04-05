"""Mode for replacing a character."""
from typing import TYPE_CHECKING

from illud.character import Character
from illud.characters import CARRIAGE_RETURN, ESCAPE, NEWLINE
from illud.mode import Mode

if TYPE_CHECKING:
    from illud.illud_state import IlludState  # pylint: disable=cyclic-import  # pragma: no cover


class Replace(Mode):  # pylint: disable=too-few-public-methods
    """Mode for replacing a character."""
    name: str = 'Replace'

    @classmethod
    def evaluate(cls, state: 'IlludState', character: Character) -> None:
        """Evaluate the character for the given state."""
        super(Replace, Replace).evaluate(state, character)

        if character.value == ESCAPE:
            from illud.modes.normal import \
                Normal  # pylint: disable=import-outside-toplevel, cyclic-import
            cls._change_mode(state, Normal())
        if character.value == CARRIAGE_RETURN:
            from illud.modes.normal import \
                Normal  # pylint: disable=import-outside-toplevel, cyclic-import
            state.cursor.replace(NEWLINE)
            cls._change_mode(state, Normal())
        elif character.printable:
            from illud.modes.normal import \
                Normal  # pylint: disable=import-outside-toplevel, cyclic-import
            string: str = character.value
            state.cursor.replace(string)
            cls._change_mode(state, Normal())
