import random


class Die:
    def __init__(self, max_value, randomness):
        self.randomness = randomness
        self.max_value = max_value

    def __call__(self):
        return self.randomness(1, self.max_value)


def roller(max_value, randomness=random.randint):
    return Die(max_value, randomness)()
