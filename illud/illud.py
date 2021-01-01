"""A text buffer editor and terminal viewer."""
from illud.character import Character
from illud.command import Command
from illud.repl import REPL
from illud.terminal import Terminal


class Illud(REPL):
    """A text buffer editor and terminal viewer."""
    def __init__(self) -> None:
        self._terminal: Terminal = Terminal()

    def read(self) -> Command:
        character: Character = self._terminal.get_character()
        command: Command = Command(character)
        return command
