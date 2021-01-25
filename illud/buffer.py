"""A string buffer."""
from typing import Any, Optional, Union


class Buffer():
    """A string buffer."""
    def __init__(self, string: Optional[str] = None):
        self.string: str
        if string is None:
            self.string = ''
        else:
            self.string = string

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Buffer):
            return False

        return self.string == other.string

    def __repr__(self) -> str:
        class_name: str = self.__class__.__name__

        if self.string:

            string_representation: str
            if "'" in self.string:
                string_representation = f'"{self.string}"'
            else:
                string_representation = f"'{self.string}'"

            return f'{class_name}({string_representation})'

        return f'{class_name}()'

    def __getitem__(self, index: Union[int, slice]) -> str:
        return self.string.__getitem__(index)

    def index(self, substring: str, start: Optional[int] = None, end: Optional[int] = None) -> int:
        """Return the lowest index where the substring is found within the range. Raise ValueError
           if the substring is not found."""
        index: int = self.string.index(substring, start, end)
        return index

    def insert(self, string: str, position: int) -> None:
        """Insert a string at the given position in the buffer."""
        self.string = self.string[:position] + string + self.string[position:]
