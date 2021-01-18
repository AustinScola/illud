"""A rectangular view of a string buffer."""
from illud.buffer import Buffer
from illud.integer_position_2d import IntegerPosition2D


class Window():  # pylint: disable=too-few-public-methods
    """A rectangular view of a string buffer."""
    def __init__(self, position: IntegerPosition2D, width: int, height: int, buffer_: Buffer):
        self.position: IntegerPosition2D = position
        self.width: int = width
        self.height: int = height
        self.buffer: Buffer = buffer_
