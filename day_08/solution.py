from typing import NamedTuple
from itertools import permutations


class Signal(NamedTuple):
    inp: list[str]
    out: list[str]

def sort(s):
    return "".join(sorted(s))

def load_inputs(filename):
    with open(filename) as file:
        signals = []
        for l in file:
            inp, out = l.split("|")
            signals.append(
                Signal(
                    inp=sorted(list(map(sort, inp.strip().split())), key=len),
                    out=list(map(sort, out.strip().split())),
                )
            )
    return signals

num2pat = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg",
}

pat2num = {v: k for k, v in num2pat.items()}


def maps():
    letters = "abcdefg"
    for perm in permutations(letters):
        yield dict(zip(letters, perm))


def translate(s: str, m: dict) -> str:
    return sort(s.translate("".maketrans(m)))


def check_map_on_inputs(m: dict, inputs: list[int]) -> bool:
    translated = [translate(inp, m) for inp in inputs]
    return set(translated) == set(num2pat.values())


def find_map(s: Signal) -> dict:
    for m in maps():
        if check_map_on_inputs(m, s.inp):
            return m

def decode(s, m) -> int:
    return pat2num[translate(s, m)]


def part1(signals):
    return sum(
        sum(len(out) in (2, 3, 4, 7) for out in signal.out)
        for signal in signals
    )

def part2(signals: list[Signal]) -> int:
    total = 0
    for s in signals:
        outs = [translate(o, find_map(s)) for o in s.out]
        total += int("".join([str(pat2num[o]) for o in outs]))
    return total


signals = load_inputs("inputs.txt")
print("Solution part 1:", part1(signals))
print("Solution part 2:", part2(signals))
