import operator
from functools import reduce
from typing import Any, Iterable, List, Union


class Tumbler:
    def __init__(self, dice: List) -> None:
        self.callables = list(filter(lambda d: callable(d), dice))
        self.ints = list(filter(lambda d: isinstance(d, int), dice))

    def __call__(self) -> Union[Any, int]:
        raise NotImplementedError()


class SumTumbler(Tumbler):
    def __call__(self) -> Union[Any, int]:
        return sum([d() for d in self.callables]) + sum(self.ints)


class MulTumbler(Tumbler):
    def __call__(self) -> Union[Any, int]:
        return self._prod([d() for d in self.callables]) * self._prod(self.ints)

    @staticmethod
    def _prod(iterable: Iterable) -> int:
        return reduce(operator.mul, iterable, 1)
