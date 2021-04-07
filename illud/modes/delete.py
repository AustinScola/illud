"""Mode for deleting text."""
from typing import TYPE_CHECKING

from illud.buffer import Buffer
from illud.character import Character
from illud.characters import ESCAPE
from illud.mode import Mode

if TYPE_CHECKING:
    from illud.illud_state import IlludState  # pylint: disable=cyclic-import  # pragma: no cover


class Delete(Mode):  # pylint: disable=too-few-public-methods
    """Mode for deleting text."""
    name: str = 'Delete'

    @classmethod
    def evaluate(cls, state: 'IlludState', character: Character) -> None:
        """Evaluate the character for the given state."""
        super(Delete, Delete).evaluate(state, character)

        if character.value == ESCAPE:
            from illud.modes.normal import \
                Normal  # pylint: disable=import-outside-toplevel, cyclic-import
            cls._change_mode(state, Normal())
        elif character.value == 'l':
            line: str = state.cursor.delete_line()
            state.clipboard = Buffer(line)
            from illud.modes.normal import \
                Normal  # pylint: disable=import-outside-toplevel, cyclic-import
            cls._change_mode(state, Normal())
