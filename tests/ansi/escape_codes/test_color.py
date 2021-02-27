"""Test illud.ansi.escape_codes.color."""
from illud.ansi.escape_codes.color import INVERT, RESET


def test_reset() -> None:
    """Test illud.ansi.escape_codes.color.RESET."""
    assert RESET == '\x1b[m'


def test_invert() -> None:
    """Test illud.ansi.escape_codes.color.INVERT."""
    assert INVERT == '\x1b[7m'
