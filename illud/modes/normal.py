"""Mode for navigating and manipulating text."""
from typing import TYPE_CHECKING

from illud.character import Character
from illud.command import Command
from illud.mode import Mode
from illud.modes.insert import Insert

if TYPE_CHECKING:
    from illud.illud_state import IlludState  # pylint: disable=cyclic-import


class Normal(Mode):  # pylint: disable=too-few-public-methods
    """Mode for navigating and manipulating text."""
    @staticmethod
    def evaluate(state: 'IlludState', command: Command) -> None:
        super(Normal, Normal).evaluate(state, command)

        if command == Command(Character('i')):
            state.mode = Insert()
