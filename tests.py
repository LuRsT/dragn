import unittest
import dragn
from dragn.dice import D6
from dragn.dice import D10


class StoryTellerTestCase(unittest.TestCase):
    def test_success(self):
        o = dragn.StoryTeller()
        o.results = [4, 5, 6, 7, 8, 9]
        o.difficulty = 6
        assert o.successes == 4
        assert o.result == 1

    def test_fails(self):
        o = dragn.StoryTeller()
        o.results = [4, 5, 4, 4]
        o.difficulty = 6
        assert o.fails == 4
        assert o.result == 0

    def test_criticalfail(self):
        o = dragn.StoryTeller()
        o.results = [1, 1, 1, 5, 6, 7, 8, 9]
        o.difficulty = 8
        assert o.successes == -1
        assert o.result == -1

    def test_roll(self):
        o = dragn.StoryTeller(difficulty=6, dice=6)
        o.roll()
        assert o.fails >= 0
        assert o.result in [-1, 0, 1]
        assert len(o.results) >= 6

    def test_no_roll(self):
        o = dragn.StoryTeller(difficulty=6, dice=6)
        assert o.fails >= 0
        assert o.successes >= 0
        assert len(o.results) >= 6

class DiceTestCase(unittest.TestCase):
    def test_faces(self):
        d6 = D6()
        for i in range(1, 6):
            assert i in d6.faces

        d10 = D10()
        for i in range(1, 11):
            assert i in d10.faces


if __name__ == '__main__':
    unittest.main()
