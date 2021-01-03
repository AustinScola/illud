"""A manner of operation."""
from typing import TYPE_CHECKING, Any

from illud.command import Command

if TYPE_CHECKING:
    from illud.illud_state import IlludState  # pylint: disable=cyclic-import


class Mode():
    """A manner of operation."""
    def __eq__(self, other: Any) -> bool:
        return type(self) is type(other)

    @staticmethod
    def evaluate(state: 'IlludState', command: Command) -> None:
        """Evaluate the command for the given state."""
