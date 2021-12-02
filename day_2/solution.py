from typing import List, NamedTuple


class Move(NamedTuple):
    forward: int = 0
    down: int = 0
    up: int = 0


def load_inputs(filename) -> List[int]:
    with open(filename) as file:
        lines = [line.strip().split() for line in file]
        moves = []
        for direction, n in lines:
            n = int(n)
            if direction == "forward":
                m = Move(forward=n)
            elif direction == "down":
                m = Move(down=n)
            elif direction == "up":
                m = Move(up=n)
            else:
                raise ValueError("Unknown direction")
            moves.append(m)
    return moves



def part1(moves: List[Move]) -> None:
    down = sum(move.down for move in moves)
    up = sum(move.up for move in moves)
    forward = sum(move.forward for move in moves)
    print("solution part 1:", forward * (down-up))


def part2(moves: List[Move]) -> None:
    horizontal = 0
    depth = 0
    aim = 0
    for move in moves:
        aim += move.down
        aim -= move.up
        horizontal += move.forward
        depth += aim * move.forward
    print("solution part 2:", horizontal * depth)


if __name__ == "__main__":
    moves = load_inputs("./inputs.txt")
    part1(moves)
    part2(moves)
