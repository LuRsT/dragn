import re
from typing import Any

from dragn.dice.die import DieBuilder


def __getattr__(name: str) -> Any:
    """
    Module level __getattr__ to automatically create dice when
    one a die of non-standard sizes.
    """
    m = re.match(r"D(\d+)", name)
    if m is None:
        raise AttributeError(f"Name {name} not found")

    num = int(m.group(1))
    if not num:
        raise ValueError("Cannot create a 0-sided die")

    return DieBuilder(num)
