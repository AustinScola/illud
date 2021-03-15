"""Test illud.ansi.escape_codes.screen."""
from illud.ansi.escape_codes.screen import DISABLE_ALTERNATIVE_SCREEN, ENABLE_ALTERNATIVE_SCREEN


def test_enable_alternative_screen() -> None:
    """Test illud.ansi.escape_codes.screen.ENABLE_ALTERNATIVE_SCREEN."""
    assert ENABLE_ALTERNATIVE_SCREEN == '\x1b[?1049h'


def test_disable_alternative_screen() -> None:
    """Test illud.ansi.escape_codes.screen.DISABLE_ALTERNATIVE_SCREEN."""
    assert DISABLE_ALTERNATIVE_SCREEN == '\x1b[?1049l'
