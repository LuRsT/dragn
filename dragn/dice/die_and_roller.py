import random
from typing import Any, Callable


class Die:
    def __init__(self, max_value: int, randomness: Callable) -> None:
        self.randomness = randomness
        self.max_value = max_value

    def __call__(self) -> Any:
        return self.randomness(1, self.max_value)


def roller(max_value: int, randomness: Callable = random.randint) -> Any:
    return Die(max_value, randomness)()
