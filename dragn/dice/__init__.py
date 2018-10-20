from functools import partial

from dragn.dice.die_and_roller import roller


D4 = partial(roller, 4)
D6 = partial(roller, 6)
D8 = partial(roller, 8)
D10 = partial(roller, 10)
D12 = partial(roller, 12)
D20 = partial(roller, 20)
