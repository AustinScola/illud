"""Test illud.signal_."""
from abc import ABC
from typing import Any, Iterable

import pytest

from illud.signal_ import Signal, Signals


def test_inheritance() -> None:
    """Test illud.signal_.Signal inheritance."""
    assert issubclass(Signal, ABC)


# yapf: disable
@pytest.mark.parametrize('signal, other, expected_equality', [
    (Signal(), 'foo', False),
    (Signal(), Signal(), True),
])
# yapf: enable
def test_eq(signal: Signal, other: Any, expected_equality: bool) -> None:
    """Test illud.signal_.Signal.__eq__."""
    equality = signal == other

    assert equality == expected_equality


def test_signals() -> None:
    """Test illud.signal_.Signals."""
    assert issubclass(Signals, Iterable)
    assert Signals.__args__ == (Signal, )  # type: ignore[attr-defined]
