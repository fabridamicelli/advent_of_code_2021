from copy import deepcopy
from typing import NamedTuple


octopi = [
    [4,5,7,5,3,5,5,6,2,3],
    [3,3,2,5,5,7,8,4,2,6],
    [7,8,8,5,1,6,5,5,7,6],
    [4,8,7,1,4,5,5,6,5,8],
    [3,7,2,2,5,4,5,3,1,2],
    [8,3,6,2,6,6,3,8,3,2],
    [5,5,6,2,7,4,3,3,2,4],
    [4,1,6,5,7,7,6,4,1,2],
    [1,8,1,7,8,1,3,6,7,5],
    [4,2,5,5,5,2,4,6,3,2],
]

Grid = list[list]

class Point(NamedTuple):
    i: int
    j: int


def plus_one(octopi, points=None):
    if points is None:
        return [[elem + 1 for elem in row] for row in octopi]
    new = deepcopy(octopi)
    for p in points:
        new[p.i][p.j] += 1
    return new


def reset(octopi, points=None):
    new = deepcopy(octopi)
    for p in points:
        new[p.i][p.j] = 0
    return new


def should_flash(octopi):
    return [
        Point(i=i, j=j)
        for i, row in enumerate(octopi)
        for j, value in enumerate(row)
        if value > 9
    ]


def is_in_grid(p: Point, g: Grid) -> bool:
    n_rows, n_cols = len(g), len(g[0])
    return p.i in range(n_rows) and p.j in range(n_cols)


def neighbors(p: Point, g: Grid) -> list[Point]:
    candidates = [
        Point(i=p.i - 1, j=p.j - 1),
        Point(i=p.i - 1, j=p.j + 1),
        Point(i=p.i - 1, j=p.j),
        Point(i=p.i + 1, j=p.j),
        Point(i=p.i + 1, j=p.j - 1),
        Point(i=p.i + 1, j=p.j + 1),
        Point(i=p.i, j=p.j - 1),
        Point(i=p.i, j=p.j + 1),
    ]
    return [p for p in candidates if is_in_grid(p, g)]


def value(p: Point, g: Grid) -> int:
    return g[p.i][p.j]


def n_octopi(octopi):
    return len(octopi) * len(octopi[0])


def step(octopi):
    octopi = plus_one(octopi)
    already_flashed = set()
    n_flashes = len(already_flashed)
    while True:
        to_flash = [p for p in should_flash(octopi) if p not in already_flashed]
        for p in to_flash:
            octopi = plus_one(octopi, neighbors(p, octopi))
        already_flashed.update(to_flash)
        if len(already_flashed) == n_flashes:
            octopi = reset(octopi, already_flashed)
            all_flashed = len(already_flashed) == n_octopi(octopi)
            return octopi, n_flashes, all_flashed
        n_flashes = len(already_flashed)


def part1(octopi):
    total = 0
    for i in range(100):
        octopi, n_flashes, _ = step(octopi)
        total += n_flashes
    return total

def part2(octopi):
    n_step, all_flashed = 0, False
    while not all_flashed:
        n_step += 1
        octopi, _, all_flashed = step(octopi)
    return n_step

print("Solution part 1:", part1(octopi))
print("Solution part 2:", part2(octopi))
