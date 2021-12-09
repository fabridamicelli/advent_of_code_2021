from dataclasses import dataclass
from typing import Iterable, NamedTuple
from functools import reduce
from operator import mul


def load_inputs(filename):
    with open(filename) as file:
        return [list(map(int, line.strip())) for line in file]


Grid = list[list[int]]

def pad(g: Grid, val: int = 10) -> Grid:
    n_rows, n_cols = len(g), len(g[0])
    new_g = [[val for _ in range(n_cols+2)]]
    for row in g:
        new_g.append([val] + row + [val])
    new_g.append([val for _ in range(n_cols+2)])
    return new_g


def patches(g: Grid) -> Iterable[tuple]:
    n_rows, n_cols = len(g), len(g[0])
    for i in range(1, n_rows-1):
        for j in range(1, n_cols-1):
            yield (i, j), g[i][j], (g[i-1][j], g[i+1][j], g[i][j-1], g[i][j+1])


def is_minumum(n, neighbors):
    return all(n < neighbor for neighbor in neighbors)


class Point(NamedTuple):
    i: int
    j: int


def find_minima(g: Grid):
    return [
        Point(i=i-1, j=j-1)
        for (i,j), n, neighbors in patches(pad(g))
        if is_minumum(n, neighbors)
    ]


def is_in_grid(p: Point, g: Grid) -> bool:
    n_rows, n_cols = len(g), len(g[0])
    return p.i in range(n_rows) and p.j in range(n_cols)


def neighbors(p: Point, g: Grid) -> list[Point]:
    candidates = [
        Point(i=p.i - 1, j=p.j),
        Point(i=p.i + 1, j=p.j),
        Point(i=p.i, j=p.j - 1),
        Point(i=p.i, j=p.j + 1),
    ]
    return [p for p in candidates if is_in_grid(p, g) and value(p, g) != 9]


def value(p: Point, g: Grid) -> int:
    return g[p.i][p.j]


def find_basin(p: Point, g: Grid):
    basin = set([p])
    queue = [p]
    while queue:
        current = queue.pop()
        neigs = [n for n in neighbors(current, g) if value(n, g) > value(current, g)]
        queue += neigs
        basin.update(neigs)
    return basin


def part1(heightmap):
    return sum(
        1 + n
        for _, n, neighbors in patches(pad(heightmap))
        if is_minumum(n, neighbors)
    )

def part2(heightmap):
    minima = find_minima(heightmap)
    lens = sorted(len(find_basin(m, heightmap)) for m in minima)
    return reduce(mul, lens[-3:])


heightmap = load_inputs("inputs.txt")
print("Solution part 1:", part1(heightmap))
print("Solution part 2:", part2(heightmap))
