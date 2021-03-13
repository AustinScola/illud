"""Test illud.signals.terminal_size_change."""
from illud.signal_ import Signal
from illud.signals.terminal_size_change import TerminalSizeChange


def test_inheritance() -> None:
    """Test illud.signals.terminal_size_change.TerminalSizeChange inheritance."""
    assert issubclass(TerminalSizeChange, Signal)
