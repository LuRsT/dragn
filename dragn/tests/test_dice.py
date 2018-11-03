from functools import partial
from typing import Callable

from dragn.dice import D4, D6, D8, D10, D12, D20
from dragn.dice.die_and_roller import roller


# mypy: ignore
class TestRoller:
    def test_roller_very_naive(self) -> None:
        def fake_randomness(max_value: int, randomness: Callable) -> int:
            return 4

        result = roller(0, randomness=fake_randomness)

        assert result == 4

    def test_default_roller(self) -> None:
        result = roller(6)

        assert result in range(1, 7)

    def test_custom_roller_with_partial(self) -> None:
        die = partial(roller, 6)

        assert die() in range(1, 7)


class TestDie:
    def test_one_configured_die(self) -> None:
        assert D4() in range(1, 5)

    def test_all_configured_dice(self) -> None:
        configured_dice = {
            D4: range(1, 5),
            D6: range(1, 7),
            D8: range(1, 9),
            D10: range(1, 11),
            D12: range(1, 13),
            D20: range(1, 21),
        }
        for die, results_range in configured_dice.items():
            assert die() in results_range
