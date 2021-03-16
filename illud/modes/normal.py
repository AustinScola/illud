"""Mode for navigating and manipulating text."""
from typing import TYPE_CHECKING

from illud.character import Character
from illud.mode import Mode
from illud.modes.insert import Insert

if TYPE_CHECKING:
    from illud.illud_state import IlludState  # pylint: disable=cyclic-import # pragma: no cover


class Normal(Mode):  # pylint: disable=too-few-public-methods
    """Mode for navigating and manipulating text."""
    @staticmethod
    def evaluate(state: 'IlludState', character: Character) -> None:
        super(Normal, Normal).evaluate(state, character)

        if character.value == 'd':
            state.cursor.move_left()
            state.window.adjust_view_to_include(state.cursor.index)
        elif character.value == 'f':
            state.cursor.move_right()
            state.window.adjust_view_to_include(state.cursor.index)
        elif character.value == 'k':
            state.cursor.move_up()
            state.window.adjust_view_to_include(state.cursor.index)
        elif character.value == 'j':
            state.cursor.move_down()
            state.window.adjust_view_to_include(state.cursor.index)
        elif character.value == 'w':
            state.cursor.next_word()
            state.window.adjust_view_to_include(state.cursor.index)
        elif character.value == 'x':
            state.cursor.delete()
        elif character.value == 'i':
            state.mode = Insert()
