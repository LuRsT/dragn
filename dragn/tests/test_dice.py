from functools import partial
from typing import Callable

from dragn.dice import D4, D6, D8, D10, D12, D20
from dragn.dice.die import DieBuilder


class TestDieBuilder:
    def test_creating_one_die(self) -> None:
        my_new_die = DieBuilder(4)

        assert my_new_die() in range(1, 5)


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


class TestDieBuilderForMultiDie:
    def test_creating_dice(self) -> None:
        multi_die = D6 * 2

        assert multi_die() in range(2, 13)

    def test_creating_dice_in_different_order_of_multiplication(self) -> None:
        multi_die = 2 * D6

        assert multi_die() in range(2, 13)
