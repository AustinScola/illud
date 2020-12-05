"""Test illud.illud."""
from illud.illud import Illud


def test_run() -> None:
    """Test illud.illud.Illud.run."""
    illud: Illud = Illud()
    illud.run()
