"""Test illud.characters."""
from illud.characters import BACKSPACE, NEWLINE


def test_backspace() -> None:
    """Test illud.characters.BACKSPACE."""
    assert BACKSPACE == ''


def test_newline() -> None:
    """Test illud.characters.NEWLINE."""
    assert NEWLINE == '\n'
