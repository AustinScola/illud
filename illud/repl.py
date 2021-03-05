"""Read, evaluate, print, and then loop."""
from typing import Any

from illud.exceptions.break_exception import BreakException


class REPL():
    """Read, evaluate, print, and then loop."""
    def __call__(self) -> None:
        """Perform one-time startup, then read, evaluate, print, and loop."""
        self.startup()

        while True:
            try:
                input_: Any = self.read()
                result: Any = self.evaluate(input_)
                self.print(result)
            except BreakException:
                return
            except Exception as exception:  # pylint: disable=broad-except
                self.catch(exception)
                return

    def startup(self) -> None:
        """Perform one-time startup."""

    def read(self) -> Any:
        """Return the next input."""

    def evaluate(self, input_: Any) -> Any:
        """Return the evaluated result of the input."""

    def print(self, result: Any) -> None:
        """Output the result of evaluation."""

    def catch(self, exception: Exception) -> None:  # pylint: disable=no-self-use
        """Handle exceptions."""
        raise exception
