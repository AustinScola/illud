"""A manner of operation."""
from typing import TYPE_CHECKING, Any

from seligimus.python.decorators.operators.equality.equal_type import equal_type

from illud.characters import CONTROL_C
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
    def evaluate(state: 'IlludState', command: Command) -> None:  # pylint: disable=unused-argument
        """Evaluate the command for the given state."""
        if command.character.value == CONTROL_C:
            raise QuitException
