"""Input to illud."""
from abc import ABC, abstractmethod
from typing import Any, Iterator


class Input(ABC):
    """Input to illud."""
    @abstractmethod
    def __next__(self) -> Any:
        """Return the next input."""
        raise NotImplementedError

    def __iter__(self) -> Iterator[Any]:
        """Yield the next input."""
        return self
