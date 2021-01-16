"""Test illud.ansi.escape_codes.cursor."""
from illud.ansi.escape_codes.cursor import DEVICE_STATUS_REPORT


def test_clear_screen() -> None:
    """Test illud.ansi.escape_codes.cursor.DEVICE_STATUS_REPORT."""
    assert DEVICE_STATUS_REPORT == '\x1b[6n'
