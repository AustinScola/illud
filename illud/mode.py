"""A manner of operation."""
from typing import TYPE_CHECKING, Any

from seligimus.maths.integer_position_2d import IntegerPosition2D
from seligimus.python.decorators.operators.equality.equal_type import equal_type

from illud.characters import CONTROL_C, CONTROL_D, CONTROL_F, CONTROL_J, CONTROL_K
from illud.command import Command
from illud.exceptions.quit_exception import QuitException

if TYPE_CHECKING:
    from illud.illud_state import IlludState  # pylint: disable=cyclic-import


class Mode():
    """A manner of operation."""
    @equal_type
    def __eq__(self, other: Any) -> bool:
        return True

    @staticmethod
    def evaluate(state: 'IlludState', command: Command) -> None:
        """Evaluate the command for the given state."""
        if command.character.value == CONTROL_C:
            raise QuitException

        if command.character.value == CONTROL_D:
            left = IntegerPosition2D(-1, 0)
            state.window.move_view(left)
        elif command.character.value == CONTROL_F:
            right = IntegerPosition2D(1, 0)
            state.window.move_view(right)
        elif command.character.value == CONTROL_J:
            down = IntegerPosition2D(0, 1)
            state.window.move_view(down)
        elif command.character.value == CONTROL_K:
            up = IntegerPosition2D(0, -1)  # pylint: disable=invalid-name
            state.window.move_view(up)
