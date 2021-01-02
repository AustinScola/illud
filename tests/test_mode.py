"""Test illud.mode."""
from typing import Any

import pytest

from illud.mode import Mode


# yapf: disable
@pytest.mark.parametrize('mode, other, expected_equality', [
    (Mode(), 'foo', False),
    (Mode(), 1, False),
    (Mode(), Mode(), True),
])
# yapf: enable
def test_eq(mode: Mode, other: Any, expected_equality: bool) -> None:
    """Test illud.mode.__eq__."""
    equality: bool = mode == other

    assert equality == expected_equality
