"""Test illud.signal_handler."""
from unittest.mock import patch

import pytest
from seligimus.maths.integer_position_2d import IntegerPosition2D
from seligimus.maths.integer_size_2d import IntegerSize2D

from illud.canvas import Canvas
from illud.illud_state import IlludState
from illud.signal_ import Signal
from illud.signal_handler import SignalHandler
from illud.signals.terminal_size_change import TerminalSizeChange
from illud.status_bar import StatusBar
from illud.window import Window


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('state_before, signal, terminal_size, expected_state_after', [
    (IlludState(), TerminalSizeChange(), IntegerSize2D(120, 80), IlludState(terminal_size=IntegerSize2D(120, 80), canvas=Canvas(IntegerSize2D(120, 80)).fill(' '), window=Window(size=IntegerSize2D(120, 79)), status_bar=StatusBar(IntegerPosition2D(0, 79), IntegerSize2D(120, 1)))),
])
# yapf: enable # pylint: enable=line-too-long
def test_handle(state_before: IlludState, signal: Signal, terminal_size: IntegerSize2D,
                expected_state_after: IlludState) -> None:
    """Test illud.signal_handler.SignalHandler.handle."""
    signal_handler: SignalHandler = SignalHandler()

    with patch('illud.illud.Terminal.get_size', return_value=terminal_size):
        signal_handler.handle(state_before, signal)

    assert state_before == expected_state_after
