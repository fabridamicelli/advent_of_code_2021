def load_inputs(filename):
    with open(filename) as file:
        return list(map(int, file.read().strip().split(",")))


def part1(pos: list[int]):
    return min(
        sum(abs(crab-p) for crab in pos if crab != p)
        for p in range(max(pos))
    )


def incremental_cost(cost: int) -> int:
    return sum(c for c in range(1, cost+1))


def part2(pos: list[int]):
    return min(
        sum(incremental_cost(abs(crab-p)) for crab in pos if crab != p)
        for p in range(max(pos))
    )

pos = load_inputs("inputs.txt")
print("Solution part 1:", part1(pos))
print("Solution part 2:", part2(pos))
