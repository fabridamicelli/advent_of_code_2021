from functools import partial
from itertools import chain, zip_longest, starmap
from operator import or_, xor


def load_inputs(filename):
    points = []
    with open(filename) as file:
        for line in file:
            x, y = line.strip().split(",")
            points.append((int(x), int(y)))
    return points



def make_array(points):
    max_x = max(x for x,_ in points)
    max_y = max(y for _,y in points)
    return [
        [1 if (x, y) in points else 0 for x in range(max_x+1)]
        for y in range(max_y+1)
    ]

def transpose(array):
    return list(zip(*array))

def split(seq, i):
    return seq[:i], seq[i+1:]

def aligned_pairs(seq1, seq2):
    return list(zip_longest(reversed(seq1), reversed(seq2), fillvalue=0))

def fold_row(seq, i=None):
    left, right = split(seq, i)
    return list(starmap(or_, aligned_pairs(left, right[::-1])))[::-1]

def _fold_array(array, i=None):
    return list(map(partial(fold_row, i=i), array))

def fold(array, x=False, y=False):
    assert xor(x, y)
    if x:
        return _fold_array(array, i=x)
    return transpose(_fold_array(transpose(array), i=y))

def part1(points):
    return sum(chain(*fold(make_array(points), x=655)))

def part2(points):
    instructions = [
        "x,655", "y,447", "x,327", "y,223", "x,163",
        "y,111", "x,81", "y,55", "x,40", "y,27", "y,13", "y,6",
    ]
    array = make_array(points)
    for instruction in instructions:
        direction, n = instruction.split(",")
        array = fold(
            array,
            x=int(n) if direction == "x" else False,
            y=int(n) if direction == "y" else False
        )
    return array


points = load_inputs("points.txt")
print("Solution part 1", part1(points))
print("Solution part 2", part2(points))
