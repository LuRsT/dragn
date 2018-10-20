dragn
=====

Dice System library (aka random.randint as dice)

A library that makes something simple like a random integer even simpler.

Or at least, makes it look a bit more like rolling dice.

```python
>> from dragn.dice import D6
>>> D6()
1
>>> from dragn.dice import D8
>>> f"You roll the die and the result is {D8()}"
'You roll the die and the result is 4'
>>> f"You roll 3 dice and you get {[D8() for _ in range(3)]}"
>>> 'You roll 3 dice and you get [3, 1, 8]'
```
