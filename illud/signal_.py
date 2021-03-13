"""A notification to a process or thread."""
from abc import ABC
from typing import Any

from seligimus.python.decorators.operators.equality.equal_type import equal_type


class Signal(ABC):  # pylint: disable=too-few-public-methods
    """A notification to a process or thread."""
    @equal_type
    def __eq__(self, other: Any) -> bool:
        return True
