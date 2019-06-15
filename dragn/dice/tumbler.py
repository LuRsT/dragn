from typing import Any, List, Tuple


class Tumbler:
    def __init__(self, dice: List) -> None:
        self.callables = list(filter(lambda d: callable(d), dice))
        self.ints = list(filter(lambda d: isinstance(d, int), dice))

    def __call__(self) -> Tuple[Any, ...]:
        raise NotImplementedError()


class SumTumbler(Tumbler):
    def __init__(self, dice: List) -> None:
        super().__init__(dice)

        if len(self.ints):
            raise TypeError("Cannot use integers in SumTumbler")

    def __call__(self) -> Tuple[Any, ...]:
        dice = [die for die in self.callables if not isinstance(die, SumTumbler)]
        tumblers = [
            tumbler for tumbler in self.callables if isinstance(tumbler, SumTumbler)
        ]

        return tuple([d() for d in dice]) + tuple(*[t() for t in tumblers])


class MulTumbler(Tumbler):
    def __init__(self, dice: List) -> None:
        super().__init__(dice)

        if not len(self.callables) or not len(self.ints):
            raise TypeError("Cannot multiply callables in MulTumbler")

    def __call__(self) -> Tuple[Any, ...]:
        return tuple([self.callables[0]() for _ in range(self.ints[0])])
