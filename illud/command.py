"""A key command."""
from typing import Any

from illud.character import Character


class Command():
    """A key command."""
    def __init__(self, character: Character):
        self.character: Character = character

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Command):
            return False
        return self.character == other.character

    def __str__(self) -> str:
        return self.character.value
