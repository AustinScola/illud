"""Standard input."""
import sys
import termios
import tty
from typing import Any, List, Optional, TextIO, overload

from illud.character import Character, CharacterIterator
from illud.exceptions.invalid_number_exception import InvalidNumberException
from illud.exceptions.unexpected_input_exception import UnexpectedInputException
from illud.input import Input

TeletypeAttributes = List[Any]


class StandardInput(Input):
    """Standard input."""
    def __init__(self) -> None:
        self._stdin: TextIO = sys.stdin
        self._attributes_before: TeletypeAttributes = self._get_attributes()

        self._use_raw_mode()

        self._buffer: str = ''

    def _get_attributes(self) -> TeletypeAttributes:
        """Return the teletype attributes of the standard input."""
        return termios.tcgetattr(self._stdin)

    def _use_raw_mode(self) -> None:
        """Set the standard input file descriptor to use raw mode."""
        tty.setraw(self._stdin.fileno())

    def __next__(self) -> Character:
        character: Character = Character(self.read(1))
        return character

    def read(self, length: int) -> str:
        """Return input of the given length."""
        if not length:
            return ''

        buffer_length: int = len(self._buffer)
        if length <= len(self._buffer):
            string, self._buffer = self._buffer[:length], self._buffer[length:]
            return string

        string, self._buffer = self._buffer + self._stdin.read(length - buffer_length), ''
        return string

    def __iter__(self) -> CharacterIterator:
        raise NotImplementedError

    def __del__(self) -> None:
        self._reset_attributes()

    def _reset_attributes(self) -> None:
        termios.tcsetattr(self._stdin, termios.TCSADRAIN, self._attributes_before)

    def peek(self, length: int) -> str:
        """Return a peek of the next characters."""
        if not length:
            return ''

        buffer_length: int = len(self._buffer)

        if length <= len(self._buffer):
            return self._buffer[:length]

        new_input: str = self._stdin.read(length - buffer_length)
        self._buffer = self._buffer + new_input
        return self._buffer

    def pop(self, length: int) -> None:
        """Discard input of the given length."""
        if length == 0:
            return

        buffer_length: int = len(self._buffer)

        if length < len(self._buffer):
            self._buffer = self._buffer[length:]
        elif length == len(self._buffer):
            self._buffer = ''
        else:
            self._buffer = ''
            self._stdin.read(length - buffer_length)

    def expect(self, string: str) -> None:
        """Asserts that the input matches the expected string."""
        for expected_character in string:
            character: str = self.read(1)
            if character != expected_character:
                raise UnexpectedInputException

    def read_integer(self) -> int:
        """Return an integer."""
        string: str = ''

        while True:
            character: str = self.peek(1)
            if character.isdigit():
                self.pop(1)
                string += character
            else:
                break

        try:
            return int(string)
        except ValueError as value_error:
            raise InvalidNumberException from value_error

    @overload
    def maybe_read_integer(self, default: int) -> int:
        ...

    @overload
    def maybe_read_integer(self, default: None) -> None:
        ...

    def maybe_read_integer(self, default: Optional[int] = None) -> Optional[int]:
        """Return an integer or a default value."""
        maybe_integer: Optional[int]

        try:
            maybe_integer = self.read_integer()
        except InvalidNumberException:
            maybe_integer = default

        return maybe_integer
