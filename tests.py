import unittest
import dragn


class D10TestCase(unittest.TestCase):
    def test_success(self):
        o = dragn.D10()
        o.results = [4, 5, 6, 7, 8, 9]
        o.difficulty = 6
        assert o.successes == 4

    def test_fails(self):
        o = dragn.D10()
        o.results = [4, 5, 6, 7, 8, 9]
        o.difficulty = 6
        assert o.fails == 2

    def test_criticalfail(self):
        o = dragn.D10()
        o.results = [1, 1, 1, 5, 6, 7, 8, 9]
        o.difficulty = 8
        assert o.successes == -1

    def test_roll(self):
        o = dragn.D10(difficulty=6, dices=6)
        o.roll(rolls=5)
        assert o.fails >= 0
        assert o.successes >= 0
