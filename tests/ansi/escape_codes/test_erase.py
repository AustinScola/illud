"""Test illud.ansi.escape_codes.erase."""
from illud.ansi.escape_codes.erase import CLEAR_SCREEN


def test_clear_screen() -> None:
    """Test illud.ansi.escape_codes.erase.CLEAR_SCREEN"""
    assert CLEAR_SCREEN == '\x1b[2J'
