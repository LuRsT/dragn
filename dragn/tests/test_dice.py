from typing import Generator

import pytest
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
            assert die.max_value == max(list(results_range))
            assert str(die) == f"D{die.max_value}"


@pytest.fixture
def D1() -> Generator:
    yield DieBuilder(1)


class TestDieBuilderForMultiDie:
    def test_creating_multi_die_by_multiplication(self, D1: DieBuilder) -> None:
        multi_die = D1 * 2

        assert multi_die() == (1, 1)

    def test_creating_multi_die_by_multiplication_in_different_order(
        self, D1: DieBuilder
    ) -> None:
        multi_die = 2 * D1

        assert multi_die() == (1, 1)

    def test_creating_multi_die_by_addition(self, D1: DieBuilder) -> None:
        with pytest.raises(TypeError):
            1 + D1

    def test_creating_multi_die_by_addition_in_different_order(
        self, D1: DieBuilder
    ) -> None:
        with pytest.raises(TypeError):
            D1 + 1

    def test_creating_multi_die_by_addition_with_another_die(
        self, D1: DieBuilder
    ) -> None:
        multi_die = D1 + D1

        assert multi_die() == (1, 1)

    def test_creating_multi_die_by_addition_with_another_dice(
        self, D1: DieBuilder
    ) -> None:
        multi_die = D1 + D1 + D1
        assert multi_die() == (1, 1, 1)

    def test_creating_multi_die_by_multiplication_with_another_die(
        self, D1: DieBuilder
    ) -> None:
        with pytest.raises(TypeError):
            D1 * D1

    def test_running_dice_with_multiplication_twice(self, D1: DieBuilder) -> None:
        multi_die = 3 * D6
        assert sum(multi_die()) >= 3 <= 6 * 3
        assert sum(multi_die()) >= 3 <= 6 * 3

    def test_running_dice_with_addition_twice(self, D1: DieBuilder) -> None:
        multi_die = D6 + D6
        assert sum(multi_die()) >= 2 <= 6 * 2
        assert sum(multi_die()) >= 2 <= 6 * 2
