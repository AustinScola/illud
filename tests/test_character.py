"""Test illud.character."""
from typing import Any

import pytest

from illud.character import Character


# yapf: disable
@pytest.mark.parametrize('value', [
    ('i'),
])
# yapf: enable
def test_init(value: str) -> None:
    """Test illud.character.Character.__init__."""
    character: Character = Character(value)

    assert character.value == value


# yapf: disable
@pytest.mark.parametrize('character, other, expected_equality', [
    (Character('i'), 'foo', False),
    (Character('i'), Character('v'), False),
    (Character('i'), Character('i'), True),
])
# yapf: enable
def test_eq(character: Character, other: Any, expected_equality: bool) -> None:
    """Test illud.character.Character.__eq__."""
    equality: bool = character == other
    assert equality == expected_equality
