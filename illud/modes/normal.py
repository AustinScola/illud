"""Mode for navigating and manipulating text."""
from typing import TYPE_CHECKING, Optional

from illud.buffer import Buffer
from illud.character import Character
from illud.characters import BACKSPACE
from illud.mode import Mode
from illud.modes.delete import Delete
from illud.modes.insert import Insert
from illud.modes.replace import Replace
from illud.modes.select import Select
from illud.selection import Selection

if TYPE_CHECKING:
    from illud.illud_state import IlludState  # pylint: disable=cyclic-import # pragma: no cover


class Normal(Mode):  # pylint: disable=too-few-public-methods
    """Mode for navigating and manipulating text."""
    name: str = 'Normal'

    @classmethod
    def evaluate(cls, state: 'IlludState', character: Character) -> None:  # pylint: disable=too-many-branches
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
            cursor_character: Optional[str] = state.cursor.character
            if cursor_character is not None:
                state.clipboard = Buffer(cursor_character)
            state.cursor.delete()
        elif character.value == 'i':
            cls._change_mode(state, Insert())
        elif character.value == 's':
            cls._change_mode(state, Select())
            state.selection = Selection.from_cursor(state.cursor)
        elif character.value == 'r':
            cls._change_mode(state, Replace())
        elif character.value == 'X':
            cls._change_mode(state, Delete())
        elif character.value == 'p':
            if state.clipboard:
                state.cursor.insert(state.clipboard.string)
        elif character.value == BACKSPACE:
            state.cursor.backspace()
