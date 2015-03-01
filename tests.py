from dragn.dice.d10 import D10
from dragn.dice.d6 import D6
from dragn.storyteller import StoryTeller
from unittest import TestCase
from unittest import main as run_tests


class StoryTellerTestCase(TestCase):

    def test_success(self):
        o = StoryTeller()
        o.results = [4, 5, 6, 7, 8, 9]
        o.difficulty = 6
        assert o.successes == 4
        assert o.result == 1

    def test_fails(self):
        o = StoryTeller()
        o.results = [4, 5, 4, 4]
        o.difficulty = 6
        assert o.fails == 4
        assert o.result == 0

    def test_criticalfail(self):
        o = StoryTeller()
        o.results = [1, 1, 1, 5, 6, 7, 8, 9]
        o.difficulty = 8
        assert o.successes == -1
        assert o.result == -1

    def test_roll(self):
        o = StoryTeller(difficulty=6, dice=6)
        o.roll()
        assert o.fails >= 0
        assert o.result in [-1, 0, 1]
        assert len(o.results) >= 6

    def test_no_roll(self):
        o = StoryTeller(difficulty=6, dice=6)
        assert o.fails >= 0
        assert o.successes >= 0
        assert len(o.results) >= 6


class DiceTestCase(TestCase):
    def test_faces(self):
        d6 = D6()
        for i in range(1, 6):
            assert i in d6.faces

        d10 = D10()
        for i in range(1, 11):
            assert i in d10.faces


if __name__ == '__main__':
    run_tests()
