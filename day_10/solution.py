def load_inputs(filename):
    with open(filename) as file:
        return [line.strip() for line in file]


OPENINGS = ["[", "{", "(", "<"]
CLOSINGS = ["]", "}", ")", ">"]
close2open = dict(zip(CLOSINGS, OPENINGS))
open2close = {v: k for k, v in close2open.items()}
SCORES = {")": 3, "]": 57, "}": 1197, ">": 25137}


def find_corrupt_char(seq: str):
    line = []
    for c in seq:
        if c in OPENINGS:
            line.append(c)
        elif c in CLOSINGS:
            last_open = line.pop()
            if close2open[c] != last_open:
                return c
        else:
            raise ValueError("unknown character")

def get_inclomplete(inputs):
    return [line for line in inputs if not find_corrupt_char(line)]


def get_open(seq):
    idx_to_delete = []
    for i, (c1, c2) in enumerate(zip(seq, seq[1:])):
        if c2 in CLOSINGS and c1 == close2open[c2]:
            idx_to_delete += [i, i+1]
    new = [c for i, c in enumerate(seq) if i not in idx_to_delete]
    return None if new == seq else new


def shrink(seq):
    while True:
        new = get_open(seq)
        if new is None:
            return seq
        seq = new


def score_completion(completion):
    factor = {")": 1, "]": 2, "}": 3, ">": 4}
    total = 0
    for c in completion:
        total *= 5
        total += factor[c]
    return total


def part1(inputs):
    illegal_characters = []
    for line in inputs:
        if c := find_corrupt_char(line):
            illegal_characters.append(c)
    return sum(SCORES[c] for c in illegal_characters)


def part2(inputs):
    incomplete = get_inclomplete(inputs)
    scores = []
    for inc in incomplete:
        inc = shrink(inc)
        completion = [open2close[c] for c in reversed(inc)]
        scores.append(score_completion(completion))
    return sorted(scores)[int(len(scores)/2)]

inputs = load_inputs("inputs.txt")
print("Solution part 1:", part1(inputs))
print("Solution part 2:", part2(inputs))
