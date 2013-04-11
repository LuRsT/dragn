import random


class StoryTeller(object):
    def __init__(self, dice=None, difficulty=None, results=[]):
        self.dice       = dice
        self.difficulty = difficulty
        self._results   = results
        self._reroll    = False

    def roll(self):
        """ Rolls a die
        Stores the results in self.results and returns them also
        """
        results = []
        for i in range(self.dice):
            results += self._add_result([])
        self._results = results
        return self._results

    def _add_result(self, sub_results=[]):
        """ Recursive method that rolls a die and
        returns the value, if the value is 10 it rolls again
        """
        result = random.randint(1, 10)
        sub_results.append(result)
        if result == 10:
            self._reroll = True
            return self._add_result(sub_results)
        return sub_results


    @property
    def results(self):
        if self._results == []:
            self.roll()

        return self._results

    @results.setter
    def results(self, value):
        self._results = value

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

    @property
    def result(self):
        """
        Helper method to get the result
        Returns -1 in case of critical fail, 0 for fail and 1 for success
        """
        if self.successes < 0:
            return -1
        elif self.successes == 0:
            return 0
        else:
            return 1
