# Advent of code 2021

Pure Python (3.9) solutions for the 2021 Edition of [Advent of Code](https://adventofcode.com/).

## Learnings

- Transforming binary to decimal
Example:
```python
int("1001", 2)
>> 9
```
- Exponential (big O) scaling is painfully bad

- str translate
Example:
```python
string = "12321"
table = "".maketrans(
    {
    **{"0": "6"},
    **{str(i): str(i-1) for i in range(1,9)},
    }
)
n_offspring = sum(1 for s in ts if s == "0")
string = string.translate(table)
```
