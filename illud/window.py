"""A rectangular view of a string buffer."""
from illud.buffer import Buffer


class Window():  # pylint: disable=too-few-public-methods
    """A rectangular view of a string buffer."""
    def __init__(self, x: int, y: int, width: int, height: int, buffer_: Buffer):  # pylint: disable=too-many-arguments
        self.x: int = x  # pylint: disable=invalid-name
        self.y: int = y  # pylint: disable=invalid-name
        self.width: int = width
        self.height: int = height
        self.buffer: Buffer = buffer_
