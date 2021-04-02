"""A status bar for displaying information."""
from seligimus.maths.integer_position_2d import IntegerPosition2D

from illud.canvas import Canvas
from illud.window import Window


class StatusBar(Window):
    """A status bar for displaying information."""
    def draw(self, canvas: Canvas) -> None:
        super().draw(canvas)

        for canvas_row in range(self.position.y, self.position.y + self.size.y):
            for canvas_column in range(self.position.x, self.position.x + self.size.x):
                canvas_position: IntegerPosition2D = IntegerPosition2D(canvas_column, canvas_row)
                canvas.invert(canvas_position)
