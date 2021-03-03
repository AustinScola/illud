"""Test illud.characters."""
from illud.characters import BACKSPACE, CARRIAGE_RETURN, CONTROL_C, ESCAPE, NEWLINE


def test_backspace() -> None:
    """Test illud.characters.BACKSPACE."""
    assert BACKSPACE == ''


def test_newline() -> None:
    """Test illud.characters.NEWLINE."""
    assert NEWLINE == '\n'


def test_carriage_return() -> None:
    """Test illud.characters.CARRIAGE_RETURN."""
    assert CARRIAGE_RETURN == '\r'


def test_escape() -> None:
    """Test illud.characters.ESCAPE."""
    assert ESCAPE == ''


def test_control_c() -> None:
    """Test illud.characters.CONTROL_C."""
    assert CONTROL_C == ''
