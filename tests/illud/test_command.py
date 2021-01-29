"""Test illud.command."""
from typing import Any

import pytest

from illud.character import Character
from illud.command import Command


# yapf: disable
@pytest.mark.parametrize('character', [
    (Character('i')),
])
# yapf: enable
def test_init(character: Character) -> None:
    """Test illud.command.Command.__init__."""
    command: Command = Command(character)

    assert command.character == character


# yapf: disable
@pytest.mark.parametrize('command, other, expected_equality', [
    (Command(Character('i')), 'foo', False),
    (Command(Character('i')), Command(Character('v')), False),
    (Command(Character('i')), Command(Character('i')), True),
])
# yapf: enable
def test_eq(command: Command, other: Any, expected_equality: bool) -> None:
    """Test illud.command.Command.__eq__."""
    equality: bool = command == other
    assert equality == expected_equality


# yapf: disable
@pytest.mark.parametrize('command, expected_string', [
    (Command(Character('i')), 'i'),
])
# yapf: enable
def test_str(command: Command, expected_string: str) -> None:
    """Test illud.command.Command.__str__."""
    string: str = str(command)
    assert string == expected_string
