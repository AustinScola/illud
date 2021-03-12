"""Test illud.characters."""
from illud.characters import (BACKSPACE, CARRIAGE_RETURN, CONTROL_C, CONTROL_D, CONTROL_F,
                              CONTROL_J, CONTROL_K, CONTROL_W, ESCAPE, NEWLINE)


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


def test_control_d() -> None:
    """Test illud.characters.CONTROL_D."""
    assert CONTROL_D == ''


def test_control_f() -> None:
    """Test illud.characters.CONTROL_F."""
    assert CONTROL_F == ''


def test_control_j() -> None:
    """Test illud.characters.CONTROL_J."""
    assert CONTROL_J == '\x0a'


def test_control_k() -> None:
    """Test illud.characters.CONTROL_K."""
    assert CONTROL_K == '\x0b'


def test_control_w() -> None:
    """Test illud.characters.CONTROL_w."""
    assert CONTROL_W == ''
