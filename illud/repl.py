"""Read, evaluate, print, and then loop."""
from typing import Any

from illud.exceptions.break_exception import BreakException


class REPL():
    """Read, evaluate, print, and then loop."""
    def __call__(self) -> None:
        """Read, evaluate, print, and then loop."""
        while True:
            try:
                input_: Any = self.read()
                result: Any = self.evaluate(input_)
                self.print(result)
            except BreakException:
                return

    def read(self) -> Any:
        """Return the next input."""

    def evaluate(self, input_: Any) -> Any:
        """Return the evaluated result of the input."""

    def print(self, result: Any) -> None:
        """Output the result of evaluation."""
