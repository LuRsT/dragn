import random
import dragn


class D10(dragn):
    def __init__(self, dices=None, difficulty=None, results=[]):
        self.dices = dices
        self.difficulty = difficulty
        self.results = results
        self._reroll = False

    def roll(self, rolls=1):
        self.results = self._roll(rolls)
        return None

    def _roll(self, rolls=1):
        while rolls > 0:
            results = []
            for i in range(0, self.dices):
                results += self._add_result([])
            rolls -= 1
        return results

    def _add_result(self, sub_results=[]):
        result = random.randint(1, 10)
        sub_results.append(result)
        if result == 10:
            self._reroll = True
            return self._add_result(sub_results)
        return sub_results

    @property
    def fails(self):
        fails = 0
        for i in self.results:
            if i < self.difficulty:
                fails += 1

        return fails

    @property
    def successes(self):
        successes = 0
        for i in self.results:
            if i >= self.difficulty:
                successes += 1

        return successes - self.ones

    @property
    def ones(self):
        ones = 0
        for r in self.results:
            if r == 1:
                ones += 1
        return ones
