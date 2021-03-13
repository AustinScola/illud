"""Listens for signals and queues them."""
from queue import Empty, Queue
from signal import SIGWINCH
from signal import Signals as SignalNumber  # pylint: disable=no-name-in-module
from signal import signal as register_signal_handler
from typing import Any

from illud.exceptions.no_signals_exception import NoSignalsException
from illud.input import Input
from illud.signal_ import Signal
from illud.signals.terminal_size_change import TerminalSizeChange


class SignalListener(Input):
    """Listens for signals and queues them."""
    def __init__(self) -> None:
        self._signals: Queue = Queue()

    def __bool__(self) -> bool:
        return not self._signals.empty()

    def __next__(self) -> Signal:
        try:
            signal: Signal = self._signals.get_nowait()
        except Empty as empty_exception:
            raise NoSignalsException() from empty_exception

        return signal

    def start(self) -> None:
        """Start listening to signals."""
        register_signal_handler(SIGWINCH, self._handle_terminal_size_change)

    def _handle_terminal_size_change(
        self,
        signal_number: SignalNumber,  # pylint: disable=unused-argument
        current_stack_frame: Any  # pylint: disable=unused-argument
    ) -> None:
        """Handle terminal size change signals."""
        self._signals.put(TerminalSizeChange())
