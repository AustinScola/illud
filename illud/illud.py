"""A text buffer editor and terminal viewer."""
from typing import Optional

from illud.character import Character
from illud.command import Command
from illud.illud_state import IlludState
from illud.repl import REPL
from illud.terminal import Terminal


class Illud(REPL):
    """A text buffer editor and terminal viewer."""
    def __init__(self, initial_state: Optional[IlludState] = None) -> None:
        self._terminal: Terminal = Terminal()

        self._state: IlludState
        if initial_state is None:
            self._state = IlludState()
        else:
            self._state = initial_state

    def read(self) -> Command:
        character: Character = self._terminal.get_character()
        command: Command = Command(character)
        return command
