"""Mode for selecting text."""
from typing import TYPE_CHECKING

from illud.character import Character
from illud.characters import ESCAPE
from illud.mode import Mode

if TYPE_CHECKING:
    from illud.illud_state import IlludState  # pylint: disable=cyclic-import  # pragma: no cover


class Select(Mode):  # pylint: disable=too-few-public-methods
    """Mode for selecting text."""
    name: str = 'Select'

    @classmethod
    def evaluate(cls, state: 'IlludState', character: Character) -> None:
        """Evaluate the character for the given state."""
        super(Select, Select).evaluate(state, character)

        if character.value == ESCAPE:
            from illud.modes.normal import \
                Normal  # pylint: disable=import-outside-toplevel, cyclic-import
            cls._change_mode(state, Normal())
        elif character.value == 'f':
            if state.selection is not None:
                state.selection.expand_right()
        elif character.value == 'y':
            if state.selection is not None:
                state.clipboard = state.selection.text
                state.selection = None
            from illud.modes.normal import \
                Normal  # pylint: disable=import-outside-toplevel, cyclic-import
            cls._change_mode(state, Normal())
