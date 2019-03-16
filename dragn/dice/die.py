import random
from functools import partial
from typing import Any, Callable, Union

from dragn.dice.tumbler import MulTumbler, SumTumbler, Tumbler


class Die:
    def __init__(self, max_value: int, randomness: Callable) -> None:
        self.randomness = randomness
        self.max_value = max_value

    def __call__(self) -> Any:
        return self.randomness(1, self.max_value)


class DieBuilder:
    def __init__(self, max_value: int) -> None:
        self.the_die = partial(self._die_builder, max_value)
        self.max_value = max_value

    @staticmethod
    def _die_builder(max_value: int, randomness: Callable = random.randint) -> Any:
        return Die(max_value, randomness)()

    def __call__(self) -> Any:
        return self.the_die()

    def __mul__(self, value: Union["DieBuilder", int, Tumbler]) -> Tumbler:
        return self._multiply(value)

    def __rmul__(self, value: Union["DieBuilder", int, Tumbler]) -> Tumbler:
        return self._multiply(value)

    def _multiply(self, other_value: Union["DieBuilder", int, Tumbler]) -> Tumbler:
        return MulTumbler([self, other_value])

    def __add__(self, value: Union["DieBuilder", int, Tumbler]) -> Tumbler:
        return self._add(value)

    def __radd__(self, value: Union["DieBuilder", int, Tumbler]) -> Tumbler:
        return self._add(value)

    def _add(self, other_value: Union["DieBuilder", int, Tumbler]) -> Tumbler:
        return SumTumbler([self, other_value])

    def __str__(self) -> str:
        return f"D{self.max_value}"
