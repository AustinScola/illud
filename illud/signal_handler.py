"""Handle signals."""
from seligimus.maths.integer_position_2d import IntegerPosition2D
from seligimus.maths.integer_size_2d import IntegerSize2D

from illud.illud_state import IlludState
from illud.signal_ import Signal
from illud.signals.terminal_size_change import TerminalSizeChange
from illud.terminal import Terminal


class SignalHandler():  # pylint:disable=too-few-public-methods
    """Handle signals."""
    @staticmethod
    def handle(state: IlludState, signal: Signal) -> None:
        """Handle a signal and maybe change the state."""
        if signal == TerminalSizeChange():
            terminal_size: IntegerSize2D = Terminal.get_size()
            state.terminal_size = terminal_size
            state.canvas.resize(terminal_size)
            state.window.size = IntegerSize2D(terminal_size.x, max(terminal_size.y - 1, 0))

            state.status_bar.position = IntegerPosition2D(0, max(terminal_size.y - 1, 0))
            state.status_bar.size = IntegerSize2D(
                terminal_size.x, 1) if terminal_size.y > 1 else IntegerSize2D(terminal_size.x, 0)
