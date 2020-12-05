"""Test illud.illud."""
from illud.illud import Illud
from illud.repl import REPL


def test_inheritance() -> None:
    """Test illud.illud.Illud inheritance."""
    assert issubclass(Illud, REPL)
