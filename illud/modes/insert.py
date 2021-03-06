"""Mode for inserting text."""
from typing import TYPE_CHECKING

from illud.character import Character
from illud.characters import BACKSPACE, CARRIAGE_RETURN, ESCAPE, NEWLINE
from illud.mode import Mode

if TYPE_CHECKING:
    from illud.illud_state import IlludState  # pylint: disable=cyclic-import  # pragma: no cover


class Insert(Mode):  # pylint: disable=too-few-public-methods
    """Mode for inserting text."""
    name: str = 'Insert'

    @classmethod
    def evaluate(cls, state: 'IlludState', character: Character) -> None:
        """Evaluate the character for the given state."""
        super(Insert, Insert).evaluate(state, character)

        if character.value == ESCAPE:
            from illud.modes.normal import \
                Normal  # pylint: disable=import-outside-toplevel, cyclic-import
            cls._change_mode(state, Normal())
        elif character.value == CARRIAGE_RETURN:
            state.cursor.insert(NEWLINE)
            state.window.adjust_view_to_include(state.cursor.index)
        elif character.printable:
            string: str = character.value
            state.cursor.insert(string)
            state.window.adjust_view_to_include(state.cursor.index)
        elif character.value == BACKSPACE:
            state.cursor.backspace()
