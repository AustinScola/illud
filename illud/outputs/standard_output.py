"""Standard output."""
import sys
from typing import Any

from seligimus.python.decorators.operators.equality.equal_type import equal_type

from illud.output import Output


class StandardOutput(Output):
    """Standard output."""
    def __init__(self) -> None:
        self._stdout = sys.stdout

    @equal_type
    def __eq__(self, other: Any) -> bool:
        return True

    def write(self, string: str) -> None:
        """Write a string to the buffer."""
        self._stdout.write(string)

    def flush(self) -> None:
        """Flush the buffered output."""
        self._stdout.flush()
