"""Handle signals."""
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
            state.window.size = terminal_size
