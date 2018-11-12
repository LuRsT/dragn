import random
from functools import partial
from typing import Any, Callable, List


class Die:
    def __init__(self, max_value: int, randomness: Callable) -> None:
        self.randomness = randomness
        self.max_value = max_value

    def __call__(self) -> Any:
        return self.randomness(1, self.max_value)


class DieBuilder:
    def __init__(self, max_value: int) -> None:
        self.function = partial(self.die_builder, max_value)
        self.max_value = max_value

    @staticmethod
    def die_builder(max_value: int, randomness: Callable = random.randint) -> Any:
        return Die(max_value, randomness)()

    def __call__(self) -> Any:
        return self.function()

    def __mul__(self, value: int) -> Callable:
        return self.multiply(value)

    def __rmul__(self, value: int) -> Callable:
        return self.multiply(value)

    def __add__(self, value: Any) -> Callable:
        return self.add(value)

    def __radd__(self, value: Any) -> Callable:
        return self.add(value)

    def add(self, other_value: int) -> Callable:
        def _tumbler(dice: List) -> Callable:
            real_dice = filter(lambda d: isinstance(d, DieBuilder), dice)
            ints = filter(lambda d: isinstance(d, int), dice)
            return lambda: sum([d() for d in real_dice]) + sum(ints)

        return _tumbler([self, other_value])

    def multiply(self, other_value: int) -> Callable:
        def _tumbler(dice: List) -> Callable:
            return lambda: sum([d() for d in dice])

        return _tumbler([self.function for _ in range(other_value)])

    def __str__(self):
        return f"D{self.max_value}"
