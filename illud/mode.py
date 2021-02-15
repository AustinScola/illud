"""A manner of operation."""
from typing import TYPE_CHECKING, Any

from seligimus.python.decorators.operators.equality.equal_type import equal_type

from illud.command import Command

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
