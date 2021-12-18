from heapq import heappush, heappop


def load_inputs(filename):
    with open(filename) as file:
        return [[int(n) for n in l.strip()] for l in file]


def find_path(grid):
    start = (0, 0)
    n = len(grid)
    end = (n-1, n-1)

    q = []
    heappush(q, (0, start))

    visited = set()
    while q:
        cost, (i, j) = heappop(q)
        if (i, j) == end:
            return cost
        for ii, jj in [(i-1,j), (i+1, j), (i, j+1), (i, j-1)]:
            # Are they in grid? have we yet visited them?
            if ii in range(n) and jj in range(n) and (ii, jj) not in visited:
                point = (ii, jj)
                cost_sum = cost + grid[ii][jj]
                heappush(q, (cost_sum, point))
                visited.add(point)
    print("No path found")


def wrap(v):
    while v > 9:
        v -= 9
    return v


def tile(grid, m=5):
    n_rows = len(grid)
    n = len(grid)
    new_grid = [[0 for _ in range(n*m)] for _ in range(n*m)]
    for i in range(m):
        for j in range(m):
            for ii in range(n):
                for jj in range(n):
                    value = wrap(grid[ii][jj] + i + j)
                    new_grid[ii + n*i][jj + n*j] = value
    return new_grid


def part1():
    grid = load_inputs("inputs.txt")
    print("Solution part 1:", find_path(grid))


def part2():
    grid = load_inputs("inputs.txt")
    grid = tile(grid, 5)
    print("Solution part 2:", find_path(grid))

part1()
part2()
