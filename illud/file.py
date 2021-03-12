"""A file."""
import os
from pathlib import Path
from typing import Any, Union

from seligimus.python.decorators.operators.equality.equal_type import equal_type


class File():
    """A file."""
    def __init__(self, path: Union[str, Path]):
        self.path: Path
        if isinstance(path, str):
            self.path = Path(path)
        else:
            self.path = path

    @property
    def normalized_path(self) -> Path:
        """Return the normalized path."""
        normalized_path: Path = Path(os.path.normpath(self.path))
        return normalized_path

    @equal_type
    def __eq__(self, other: Any) -> bool:
        equality: bool = self.normalized_path == other.normalized_path
        return equality
