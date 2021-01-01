"""Standard input."""
import sys
import termios
import tty
from typing import Any, List, TextIO

from illud.character import Character, CharacterIterator
from illud.input import Input

TeletypeAttributes = List[Any]


class StandardInput(Input):
    """Standard input."""
    def __init__(self) -> None:
        self._stdin: TextIO = sys.stdin
        self._attributes_before: TeletypeAttributes = self._get_attributes()

        self._use_raw_mode()

    def _get_attributes(self) -> TeletypeAttributes:
        """Return the teletype attributes of the standard input."""
        return termios.tcgetattr(self._stdin)

    def _use_raw_mode(self) -> None:
        """Set the standard input file descriptor to use raw mode."""
        tty.setraw(self._stdin.fileno())

    def __next__(self) -> Character:
        character: Character = Character(self._stdin.read(1))
        return character

    def __iter__(self) -> CharacterIterator:
        raise NotImplementedError

    def __del__(self) -> None:
        self._reset_attributes()

    def _reset_attributes(self) -> None:
        termios.tcsetattr(self._stdin, termios.TCSADRAIN, self._attributes_before)
