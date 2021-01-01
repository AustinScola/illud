"""Test illud.input."""
from abc import ABC
from typing import Any, Iterator
from unittest.mock import MagicMock

import pytest

from illud.input import Input


def test_inheritance() -> None:
    """Test illud.input.Input inheritance."""
    assert issubclass(Input, ABC)


def test_next() -> None:
    """Test illud.input.Input.__next__."""
    input_mock = MagicMock(Input, autospec=True, __next__=Input.__next__)

    with pytest.raises(NotImplementedError):
        next(input_mock)


# yapf: disable
@pytest.mark.parametrize('next_', [
    (True),
    (1),
    ('foo'),
])
# yapf: enable
def test_iter(next_: Any) -> None:
    """Test illud.input.Input.__iter__."""
    next_mock = MagicMock(return_value=next_)
    input_mock = MagicMock(Input, autospec=True, __next__=next_mock, __iter__=Input.__iter__)

    inputs: Iterator[Any] = iter(input_mock)

    next_input: Any = next(inputs)
    assert next_input == next_
