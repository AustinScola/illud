"""A text buffer editor and terminal viewer."""
from typing import Any, Optional

from illud.character import Character
from illud.command import Command
from illud.illud_state import IlludState
from illud.mode import Mode
from illud.repl import REPL
from illud.terminal import Terminal
from illud.window import Window


class Illud(REPL):
    """A text buffer editor and terminal viewer."""
    def __init__(self, initial_state: Optional[IlludState] = None) -> None:
        self._terminal: Terminal = Terminal()
        self._terminal.clear_screen()

        self._state: IlludState
        if initial_state is None:
            self._state = IlludState()
        else:
            self._state = initial_state

    def read(self) -> Command:
        character: Character = self._terminal.get_character()
        command: Command = Command(character)
        return command

    def evaluate(self, input_: Command) -> None:
        command: Command = input_
        mode: Mode = self._state.mode
        mode.evaluate(self._state, command)

    def print(self, result: Any) -> None:
        window: Window = self._state.window
        self._terminal.draw_window(window)
