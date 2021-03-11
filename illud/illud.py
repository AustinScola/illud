"""A text buffer editor and terminal viewer."""
import sys
from typing import Any, Optional

from illud.character import Character
from illud.command import Command
from illud.cursor import Cursor
from illud.exceptions.quit_exception import QuitException
from illud.illud_state import IlludState
from illud.mode import Mode
from illud.repl import REPL
from illud.terminal import Terminal
from illud.window import Window


class Illud(REPL):
    """A text buffer editor and terminal viewer."""
    def __init__(self, initial_state: Optional[IlludState] = None) -> None:
        self._terminal: Terminal = Terminal()

        self._state: IlludState
        if initial_state is None:
            self._state = IlludState(terminal_size=self._terminal.get_size())
        else:
            self._state = initial_state

    def startup(self) -> None:
        self._terminal.clear_screen()
        self.print(None)

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

        cursor: Cursor = self._state.cursor
        self._terminal.draw_cursor(cursor, window.offset)

        self._terminal.update()

    def catch(self, exception: Exception) -> None:
        if isinstance(exception, QuitException):
            self._terminal.clear_screen()
            self._terminal.move_cursor_home()
            sys.exit()

        raise exception
