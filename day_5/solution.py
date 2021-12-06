from dataclasses import dataclass


@dataclass
class Move:
    x1: int
    y1: int
    x2: int
    y2: int

    def is_vertical(self):
        return self.x1 == self.x2

    def is_horizontal(self):
        return self.y1 == self.y2

    def is_diagonal_45(self):
        return abs(self.x1-self.x2) == abs(self.y1-self.y2)


def load_inputs(filename):
    with open(filename) as file:
        lines = [l.strip() for l in file]
    moves = []
    for l in lines:
        parsed = l.split("->")
        start, end = parsed
        x1, y1 = start.split(",")
        x2, y2 = end.split(",")
        moves.append(Move(x1=int(x1), y1=int(y1), x2=int(x2), y2=int(y2)))
    return moves


def horizontal_span(m: Move):
    if m.x2 == m.x1:
        return m.x1
    if m.x2 > m.x1:
        return list(range(m.x1, m.x2+1))
    return list(range(m.x2, m.x1+1))


def vertical_span(m: Move):
    if m.y2 == m.y1:
        return m.y1
    if m.y2 > m.y1:
        return list(range(m.y1, m.y2+1))
    return list(range(m.y2, m.y1+1))


def diagonal_span(m: Move):
    assert m.is_diagonal_45()
    if m.x2 > m.x1 and m.y2 > m.y1:
        x = range(m.x1, m.x2+1)
        y = range(m.y1, m.y2+1)
    elif m.x2 > m.x1 and m.y2 < m.y1:
        x = range(m.x1, m.x2+1)
        y = range(m.y1, m.y2-1, -1)
    elif m.x2 < m.x1 and m.y2 > m.y1:
        x = range(m.x1, m.x2-1, -1)
        y = range(m.y1, m.y2+1)
    elif m.x2 < m.x1 and m.y2 < m.y1:
        x = range(m.x2, m.x1+1)
        y = range(m.y2, m.y1+1)
    else:
        raise ValueError("wrong coordinates")
    return list(zip(x, y))


def n_overlaps(grid):
    return sum(e > 1 for row in grid for e in row)


Grid = list[list[int]]


def make_grid() -> Grid:
    return [
        [0 for _ in range(1000)]
        for _ in range(1000)
    ]


def mark_span(m: Move, grid: Grid) -> None:
    if m.is_horizontal():
        for x in horizontal_span(m):
            grid[m.y1][x] += 1
    elif m.is_vertical():
        for y in vertical_span(m):
            grid[y][m.x1] += 1
    elif m.is_diagonal_45():
        for x, y in diagonal_span(m):
            grid[y][x] += 1
    else:
        raise ValueError("unknown move type")


def part1():
    moves = load_inputs("inputs.txt")
    moves = [m for m in moves if m.is_horizontal() or m.is_vertical()]
    grid = make_grid()
    for m in moves:
        mark_span(m, grid)
    print("Solution part 1:", n_overlaps(grid))


def part2():
    moves = load_inputs("inputs.txt")
    grid = make_grid()
    for m in moves:
        mark_span(m, grid)
    print("Solution part 2:", n_overlaps(grid))


part1()
part2()
