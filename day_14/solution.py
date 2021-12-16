from copy import deepcopy
from collections import Counter
from itertools import zip_longest

def load_inputs(filename):
    with open(filename) as file:
        return dict([l.strip().split(" -> ") for l in file])


def expand(seq: str, code: dict) -> str:
    insertions = [
        code.get(a+b, "")
        for i, (a, b) in enumerate(zip(seq, seq[1:]))
    ]
    return "".join(a+b for a, b in zip_longest(seq, insertions, fillvalue=""))


def expand_pairs(pairs, code):
    new = Counter()
    for (a, b), val in pairs.items():
        insertion = code.get((a, b), "")
        if None in (a, b):
            new[(a, b)] += 1
        else:
            new[(a, insertion)] += val
            new[(insertion, b)] += val
    return new


def count(pairs):
    c = Counter()
    for (a, b), val in pairs.items():
        c[a] += val
        c[b] += val
    return {k: int(v/2) for k, v in c.items() if k}


def part1():
    seq = "SHHNCOPHONHFBVNKCFFC"
    code = load_inputs("inputs.txt")
    for _ in range(10):
        seq = expand(seq, code)
    c = Counter(seq).most_common()
    return c[0][1] - c[-1][1]


def part2():
    code = load_inputs("inputs.txt")
    code = {(a, b): val for (a, b), val in code.items()}
    seq = [None] + list("SHHNCOPHONHFBVNKCFFC") + [None]
    pairs = Counter((a, b) for a, b in zip(seq, seq[1:]))
    for _ in range(40):
        pairs = expand_pairs(pairs, code)
    s = sorted(count(pairs).values())
    return s[-1] - s[0]

print("Solution part 1:", part1())
print("Solution part 2:", part2())
