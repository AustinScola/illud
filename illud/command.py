"""A key command."""
from typing import Any

from seligimus.python.decorators.operators.equality.equal_instance_attributes import \
    equal_instance_attributes
from seligimus.python.decorators.operators.equality.equal_type import equal_type

from illud.character import Character


class Command():
    """A key command."""
    def __init__(self, character: Character):
        self.character: Character = character

    @equal_type
    @equal_instance_attributes
    def __eq__(self, other: Any) -> bool:
        return True

    def __str__(self) -> str:
        return self.character.value
