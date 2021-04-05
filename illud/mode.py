"""A manner of operation."""
from typing import TYPE_CHECKING, Any

from seligimus.python.decorators.operators.equality.equal_type import equal_type
from seligimus.python.decorators.standard_representation import standard_representation

from illud.buffer import Buffer
from illud.character import Character
from illud.characters import CONTROL_C, CONTROL_D, CONTROL_F, CONTROL_J, CONTROL_K, CONTROL_W
from illud.exceptions.quit_exception import QuitException

if TYPE_CHECKING:
    from illud.illud_state import IlludState  # pylint: disable=cyclic-import # pragma: no cover


class Mode():
    """A manner of operation."""
    name: str = ''

    @equal_type
    def __eq__(self, other: Any) -> bool:
        return True

    @standard_representation
    def __repr__(self) -> str:
        pass  # pragma: no cover

    @classmethod
    def evaluate(cls, state: 'IlludState', character: Character) -> None:
        """Evaluate the character for the given state."""
        if character.value == CONTROL_C:
            raise QuitException

        if character.value == CONTROL_D:
            state.window.move_view_left()
        elif character.value == CONTROL_F:
            state.window.move_view_right()
        elif character.value == CONTROL_J:
            state.window.move_view_down()
        elif character.value == CONTROL_K:
            state.window.move_view_up()
        elif character.value == CONTROL_W:
            if state.file is not None:
                state.file.write(state.buffer)

    @staticmethod
    def _change_mode(state: 'IlludState', mode: 'Mode') -> None:
        """Change the current mode."""
        state.status_bar.buffer = Buffer(mode.name)
        state.mode = mode
