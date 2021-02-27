"""Test illud.ansi.escape_codes.color."""
from illud.ansi.escape_codes.color import RESET


def test_reset() -> None:
    """Test illud.ansi.escape_codes.color.RESET."""
    assert RESET == '\x1b[m'
