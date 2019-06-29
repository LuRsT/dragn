<p align="center">
    <img src="https://raw.githubusercontent.com/lurst/dragn/master/dragn_logo.png" alt="Dragn Logo">
</p>

<p align="center">
    <a href="https://pypi.org/project/dragn/"><img alt="Supported Python versions" src="https://img.shields.io/pypi/pyversions/dragn.svg"></a>
    <a href="https://pypi.org/project/dragn/"><img alt="PyPI version" src="https://img.shields.io/pypi/v/dragn.svg"></a>
    <a href="https://travis-ci.org/LuRsT/dragn"><img alt="Build Status" src="https://travis-ci.org/LuRsT/dragn.svg?branch=master"></a>
    <a href="https://codecov.io/gh/LuRsT/dragn"><img alt="Codecoverage" src="https://codecov.io/gh/LuRsT/dragn/branch/master/graph/badge.svg"></a>
    <a href="https://opensource.org/licenses/MIT"><img alt="Licence" src="https://img.shields.io/github/license/LuRsT/dragn.svg"></a>
    <a href="https://github.com/ambv/black"><img alt="Code style: Black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
    <a href="https://pepy.tech/badge/dragn"><img alt="Downloads" src="https://img.shields.io/pypi/dm/dragn.svg"></a>
</p>

___

<p align="center">
    <em>Roll dice in your python programs</em>
</p>

___

### Why?

I wanted a better API to rolling dice using Python, and the usual `random.randint` is very good,
but doesn't really represent rolling dice quite the way I imagine it.

This was a good learning experiment, but I'm not expecting anyone to use it.


### Who is this for?

People building RPGs, or games that would involve dice and who care about how their code looks
like.

I may be biased, but I really believe that this library provides a much better interface than
pure `random.randint`.


### How to install

```shell
$ pip install dragn
```


### How to use

```python
>> from dragn.dice import D4, D6, D8
>>> D6()
1
>>> f"You roll the die and the result is {D8()}"
'You roll the die and the result is 4'
>>> f"You roll 3 dice and you get {[D8() for _ in range(3)]}"
>>> 'You roll 3 dice and you get [3, 1, 8]'
>>> four_dice = D4 * 4
>>> f"You roll 4 dice and the results are {four_dice()}"
'You roll 4 dice and the results are (4, 3, 1, 2)'
>>> f"You roll two dice and the results are {two_dice()}"
'You roll two dice and the results are (3, 4)'
>>> dice_tower = (D6 * 2) + D4
>>> f"You roll two D6 and a D4 and check the results {dice_tower()}"
'You roll two D6 and a D4 and check the results (2, 2, 6)'
```

For more examples, check the [tests](https://github.com/LuRsT/dragn/blob/master/dragn/tests/test_dice.py)
