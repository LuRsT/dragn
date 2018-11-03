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

    @staticmethod
    def die_builder(max_value: int, randomness: Callable = random.randint) -> Any:
        return Die(max_value, randomness)()

    def __call__(self) -> Any:
        return self.function()

    def __mul__(self, value: int) -> Callable:
        return self.multiply(value)

    def __rmul__(self, value: int) -> Callable:
        return self.multiply(value)

    def multiply(self, other_value: int) -> Callable:
        def _roller(dice: List) -> Callable:
            return lambda: sum([d() for d in dice])

        return _roller([self.function for _ in range(other_value)])
