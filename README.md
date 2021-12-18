# Advent of code 2021

Pure Python (3.9) solutions for the 2021 Edition of [Advent of Code](https://adventofcode.com/).

## Learnings

- Transforming binary to decimal  
```python
int("1001", 2)
>> 9
```
- `str` method `translate`  
```python
string = "01234"
table = "".maketrans({"4": "777", "0": "22"})
string.translate(table)
>> "22123777"

- heapq out of the box

```python
from heapq import heapify, heappop

l = [4,2,4,125,5]
heapify(l)   # convert list to heap 
heappop(l)
>> 2
```
```python
