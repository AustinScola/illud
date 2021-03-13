"""Test illud.inputs.signal_listener."""
from queue import Queue
from signal import SIGWINCH
from typing import List, Optional, Type
from unittest.mock import MagicMock, patch

import pytest

from illud.exceptions.no_signals_exception import NoSignalsException
from illud.input import Input
from illud.inputs.signal_listener import SignalListener
from illud.signal_ import Signal, Signals
from illud.signals.terminal_size_change import TerminalSizeChange


def test_inheritance() -> None:
    """Test illud.inputs.signal_listener.SignalListener inheritance."""
    assert issubclass(SignalListener, Input)


def test_init() -> None:
    """Test illud.inputs.signal_listener.SignalListener.__init__."""
    signal_listener: SignalListener = SignalListener()

    assert signal_listener._signals.queue == Queue().queue  # pylint: disable=protected-access


# yapf: disable
@pytest.mark.parametrize('signal_listener, signals, expected_truthiness', [
    (SignalListener(), [], False),
    (SignalListener(), [TerminalSizeChange()], True),
    (SignalListener(), [TerminalSizeChange(), TerminalSizeChange()], True),
])
# yapf: enable
def test_bool(signal_listener: SignalListener, signals: List[Signal],
              expected_truthiness: bool) -> None:
    """Test illud.inputs.signal_listener.SignalListener.__bool__."""
    signal_queue: Queue = Queue()
    for signal in signals:
        signal_queue.put_nowait(signal)

    signal_listener._signals = signal_queue  # pylint: disable=protected-access

    truthy: bool = bool(signal_listener)

    assert truthy == expected_truthiness


# yapf: disable
@pytest.mark.parametrize('signals, expected_signal, expected_exception', [
    ([], None, NoSignalsException),
    ([TerminalSizeChange], TerminalSizeChange, None),
])
# yapf: enable
def test_next(signals: List[Signal], expected_signal: Optional[Signal],
              expected_exception: Optional[Type[BaseException]]) -> None:
    """Test illud.inputs.signal_listener.SignalListener.__next__."""
    signal_listener: SignalListener = SignalListener()

    signal_queue: Queue = Queue()
    for signal in signals:
        signal_queue.put_nowait(signal)

    signal_listener._signals = signal_queue  # pylint: disable=protected-access

    if expected_exception is None:
        signal = next(signal_listener)

        assert signal == expected_signal
    else:
        with pytest.raises(expected_exception):
            next(signal_listener)


def test_start() -> None:
    """Test illud.inputs.signal_listener.SignalListener.start."""
    signal_listener: SignalListener = SignalListener()

    with patch('illud.inputs.signal_listener.register_signal_handler') as signal_mock:
        signal_listener.start()

        signal_mock.assert_called_once_with(SIGWINCH, signal_listener._handle_terminal_size_change)  # pylint: disable=protected-access


# yapf: disable
@pytest.mark.parametrize('signals, expected_signals_after', [
    ([], [TerminalSizeChange()]),
    ([TerminalSizeChange()], [TerminalSizeChange(), TerminalSizeChange()]),
])
# yapf: enable
def test_handle_terminal_size_change(signals: Signals, expected_signals_after: Signals) -> None:
    """Test illud.inputs.signal_listener.SignalListener._handle_terminal_size_change."""
    signal_listener: SignalListener = SignalListener()

    signal_queue: Queue = Queue()
    for signal in signals:
        signal_queue.put_nowait(signal)

    expected_signal_queue: Queue = Queue()
    for expected_signal in expected_signals_after:
        expected_signal_queue.put_nowait(expected_signal)

    signal_listener._signals = signal_queue  # pylint: disable=protected-access

    signal_number = MagicMock()
    current_stack_frame = MagicMock()

    signal_listener._handle_terminal_size_change(signal_number, current_stack_frame)  # pylint: disable=protected-access

    assert signal_listener._signals.queue == expected_signal_queue.queue  # pylint: disable=protected-access
