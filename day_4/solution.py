from typing import Union


def strs2list(board: list[str]) -> list[list]:
    board = [l.split(" ") for l in board]
    return [[int(n) for n in line if n != ""] for line in board]


def load_inputs(filename) -> tuple[list, list[list]]:
    with open(filename) as file:
        lines = [line.strip() for line in file]
    lines = [line for line in lines if line != ""]
    numbers = list(map(int, lines[0].split(",")))
    boards = lines[1:]
    boards = [boards[i: i+5] for i in range(0, len(boards), 5)]
    return numbers, list(map(strs2list, boards))


Line = list[int]
Board = list[Line]


def mark(b: Board, n: int) -> Board:
    """Mark the board with -1 at the position of n - if n is there"""
    return [[-1 if num == n else num for num in line] for line in b]


def check_line(line: Line) -> bool:
    return all(n == -1 for n in line)


def check_rows(b: Board) -> bool:
    return any(check_line(row) for row in b)


def check_cols(b: Board) -> bool:
    n_cols = len(b[0])
    cols = [[row[i] for row in b] for i in range(n_cols)]
    return any(check_line(col) for col in cols)


def count_non_marked(b: Board) -> int:
    return sum(n for row in b for n in row if n != -1)


def check_board(b: Board) -> int:
    return check_cols(b) or check_rows(b)


def check_boards(bs: list[Board]) -> Union[bool, Board]:
    for b in bs:
        if check_board(b):
            return b
    return False


def part1(numbers, boards):
    for n in numbers:
        boards = [mark(board, n) for board in boards]
        winner = check_boards(boards)
        if winner:
            return count_non_marked(winner) * n


def part2(numbers, boards):
    winners = []
    for n in numbers:
        boards = [mark(board, n) for board in boards]
        for b in boards:
            if check_board(b):
                winners.append(b)
                boards.remove(b)
        if not boards:
            return count_non_marked(winners[-1]) * n


if __name__ == "__main__":
    numbers, boards = load_inputs("inputs.txt")
    print("solution part 1:", part1(numbers, boards))
    print("solution part 2:", part2(numbers, boards))
