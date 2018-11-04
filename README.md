Dragn
=====

[![PyPI version](https://img.shields.io/pypi/v/dragn.svg)](https://pypi.org/project/dragn/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/dragn.svg)](https://pypi.org/project/dragn/)
[![Build Status](https://travis-ci.org/LuRsT/dragn.svg?branch=master)](https://travis-ci.org/LuRsT/dragn)
[![codecov](https://codecov.io/gh/LuRsT/dragn/branch/master/graph/badge.svg)](https://codecov.io/gh/LuRsT/dragn)
[![License](https://img.shields.io/github/license/LuRsT/dragn.svg)](LICENSE)
[![Downloads](https://pepy.tech/badge/dragn)](https://pepy.tech/project/dragn)
[![Code style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)


Dice system library (aka `random.randint` as dice).

A library that makes something simple like a random integer even simpler.

Or at least, makes it look a bit more like rolling dice.


### How to install

```shell
$ pip install dragn
```


### How to use

```python
>> from dragn.dice import D6
>>> D6()
1
>>> from dragn.dice import D8
>>> f"You roll the die and the result is {D8()}"
'You roll the die and the result is 4'
>>> f"You roll 3 dice and you get {[D8() for _ in range(3)]}"
>>> 'You roll 3 dice and you get [3, 1, 8]'
>>> from dragn.dice import D4
>>> four_dice = D4 * 4
>>> f"You roll 4 dice and the sum is {four_dice()}"
'You roll 4 dice and the sum is 15'
>>> f"You roll 4 dice again and the sum is {four_dice()}"
'You roll 4 dice again and the sum is 13'
```
