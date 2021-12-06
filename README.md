# Advent of code 2021

Pure Python (3.9) solutions for the 2021 Edition of [Advent of Code](https://adventofcode.com/).

## Learnings

- Transforming binary to decimal  
Example:
```python
int("1001", 2)
>> 9
```
- `str` method `translate`
Example:
```python
string = "01234"
table = "".maketrans(
    {
        "4": "777",
        "0": "22"
    }
)
string.translate(table)
>> "22123777"
```
