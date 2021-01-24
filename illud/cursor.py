"""A position in a string buffer."""
from illud.buffer import Buffer


class Cursor():  # pylint: disable=too-few-public-methods
    """A position in a string buffer."""
    def __init__(self, buffer_: Buffer, position: int):
        self.buffer: Buffer = buffer_
        self.position: int = position
