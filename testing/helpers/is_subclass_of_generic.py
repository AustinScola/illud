"""Check if a type is a subclass of a generic."""
from typing import Type


def is_subclass_of_generic(class_: Type, generic_class: Type) -> bool:
    """Return whether or not a class is a subclass of a generic class."""
    original_bases = class_.__orig_bases__

    # yapf: disable
    return any(
        original_base == generic_class
        and original_base.__args__ == generic_class.__args__
        for original_base in original_bases
    )
    # yapf: enable
