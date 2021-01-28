"""Test testing.helpers.is_subclass_of_generic."""
from typing import Generic, List, Type, TypeVar

import pytest

from testing.helpers.is_subclass_of_generic import is_subclass_of_generic

T = TypeVar('T')  # pylint: disable=invalid-name


class GenericBaseClass(Generic[T]):  # pylint: disable=too-few-public-methods
    """A generic base class with a single type variable."""


class Class(GenericBaseClass[int]):  # pylint: disable=too-few-public-methods
    """A class which subclasses the generic base class with integer passed as the type variable."""


# yapf: disable
@pytest.mark.parametrize('class_, generic_class, expected_is_subclass', [
    (Class, List[int], False),
    (Class, GenericBaseClass[int], True),
    (Class, GenericBaseClass[float], False),
])
# yapf: enable
def test_is_subclass_of_generic(class_: Type, generic_class: Type,
                                expected_is_subclass: bool) -> None:
    """Test testing.helpers.is_subclass_of_generic.is_subclass_of_generic."""
    is_subclass: bool = is_subclass_of_generic(class_, generic_class)

    assert is_subclass == expected_is_subclass
