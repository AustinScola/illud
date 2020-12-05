"""Read, evaluate, print, and then loop."""
from typing import Any

from illud.exceptions.break_exception import BreakException


class REPL():
    """Read, evaluate, print, and then loop."""
    def __call__(self) -> None:
        """Read, evaluate, print, and then loop."""
        while True:
            try:
                self.read()
                self.evaluate()
                self.print()
            except BreakException:
                return

    def read(self) -> Any:
        """Return the next input."""

    def evaluate(self) -> Any:
        """Return the evaluated result of the input."""

    def print(self) -> None:
        """Output the result of evaluation."""
