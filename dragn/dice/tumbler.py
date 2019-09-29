from itertools import chain
from typing import Any, List, Tuple, Union


class Tumbler:
    def __init__(self, dice: List) -> None:
        self.callables = list(filter(lambda d: callable(d), dice))
        self.ints = list(filter(lambda d: isinstance(d, int), dice))

    def __call__(self) -> Tuple[Any, ...]:
        raise NotImplementedError()

    def __rmul__(self, other_value: Union[Any]) -> Any:
        return MulTumbler([self for i in range(other_value)])

    def __mul__(self, other_value: Union[Any]) -> Any:
        return MulTumbler([self for i in range(other_value)])

    def __add__(self, other_value: Union[Any]) -> Any:
        return SumTumbler([self, other_value])


class SumTumbler(Tumbler):
    def __init__(self, dice: List) -> None:
        super().__init__(dice)

        if len(self.ints):
            raise TypeError("Cannot use integers in SumTumbler")

    def __call__(self) -> Tuple[Any, ...]:
        def is_a_tumbler(d: Any) -> bool:
            return isinstance(d, SumTumbler) or isinstance(d, MulTumbler)

        dice = [c for c in self.callables if not is_a_tumbler(c)]
        tumblers = [c for c in self.callables if is_a_tumbler(c)]

        dice_results = tuple([d() for d in dice])
        tumbler_results = tuple(chain.from_iterable([t() for t in tumblers]))
        return dice_results + tumbler_results


class MulTumbler(Tumbler):
    def __init__(self, dice: List) -> None:
        super().__init__(dice)

    def __call__(self) -> Tuple[Any, ...]:
        if self.ints and self.callables:
            results = tuple([self.callables[0]() for _ in range(self.ints[0])])
        else:
            results = tuple(chain.from_iterable([c() for c in self.callables]))
        return results
