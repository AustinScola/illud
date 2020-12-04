"""Test illud.main"""
from typing import List

import pytest

from illud.main import main


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('arguments, expected_return_value', [
    ([], 0),
])
# yapf: enable # pylint: enable=line-too-long
def test_main(arguments: List[str], expected_return_value: int) -> None:
    """Test illud.main.main."""
    return_value: int = main(arguments)

    assert return_value == expected_return_value
