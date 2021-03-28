"""Mode for navigating and manipulating text."""
from typing import TYPE_CHECKING

from illud.character import Character
from illud.mode import Mode
from illud.modes.insert import Insert
from illud.modes.select import Select
from illud.selection import Selection

if TYPE_CHECKING:
    from illud.illud_state import IlludState  # pylint: disable=cyclic-import # pragma: no cover


class Normal(Mode):  # pylint: disable=too-few-public-methods
    """Mode for navigating and manipulating text."""
    @staticmethod
    def evaluate(state: 'IlludState', character: Character) -> None:  # pylint: disable=too-many-branches
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
        elif character.value == 'D':
            state.cursor.move_to_line_start()
            state.window.adjust_view_to_include(state.cursor.index)
        elif character.value == 'F':
            state.cursor.move_to_line_end()
            state.window.adjust_view_to_include(state.cursor.index)
        elif character.value == 'K':
            state.cursor.move_to_first_line()
            state.window.adjust_view_to_include(state.cursor.index)
        elif character.value == 'J':
            state.cursor.move_to_last_line()
            state.window.adjust_view_to_include(state.cursor.index)
        elif character.value == 'w':
            state.cursor.next_word()
            state.window.adjust_view_to_include(state.cursor.index)
        elif character.value == 'x':
            state.cursor.delete()
        elif character.value == 'i':
            state.mode = Insert()
        elif character.value == 's':
            state.mode = Select()
            state.selection = Selection.from_cursor(state.cursor)
        elif character.value == 'p':
            if state.clipboard:
                state.cursor.insert(state.clipboard.string)
