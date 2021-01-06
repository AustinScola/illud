"""Standard output."""
import sys

from illud.output import Output


class StandardOutput(Output):
    """Standard output."""
    def __init__(self) -> None:
        self._stdout = sys.stdout

    def write(self, string: str) -> None:
        """Write a string to the buffer."""
        self._stdout.write(string)

    def flush(self) -> None:
        """Flush the buffered output."""
        self._stdout.flush()
