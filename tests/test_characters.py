"""Test illud.characters."""
from illud.characters import (BACKSPACE, CARRIAGE_RETURN, CONTROL_C, CONTROL_D, CONTROL_F,
                              CONTROL_J, CONTROL_K, CONTROL_W, ESCAPE, FORM_FEED, NEWLINE, SPACE,
                              TAB, VERTICAL_TAB, WHITESPACE)


def test_space() -> None:
    """Test illud.characters.SPACE."""
    assert SPACE == ' '


def test_tab() -> None:
    """Test illud.characters.TAB."""
    assert TAB == '\t'


def test_vertical_tab() -> None:
    """Test illud.characters.VERTICAL_TAB."""
    assert VERTICAL_TAB == '\x0b'


def test_form_feed() -> None:
    """Test illud.characters.FORM_FEED."""
    assert FORM_FEED == '\x0c'


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


def test_whitespace() -> None:
    """Test illud.characters.CONTROL_w."""
    assert WHITESPACE == {SPACE, TAB, VERTICAL_TAB, CARRIAGE_RETURN, NEWLINE, FORM_FEED}
