from collections import Counter
from operator import not_


def load_inputs(filename) -> list[str]:
    with open(filename) as file:
        return [line.strip() for line in file]


def get_columns(inputs):
    for column in zip(*inputs):
        yield column


def get_common(column: list[str], most: bool) -> str:
    most_common = Counter(column).most_common(2)
    if len(most_common) == 1:
        return most_common[0][0]
    (val1, n1), (val2, n2) = most_common
    if n1 == n2:
        return "1" if most else "0"
    return val1 if most else val2


def apply_criterion(inputs: list[str], criterion="oxy"):
    assert criterion in ("oxy", "co2")
    n_cols = len(inputs[0])
    for i in range(n_cols):
        col = [inp[i] for inp in inputs]
        to_match = get_common(col, most=True if criterion == "oxy" else False)
        new_inputs = [inp for inp in inputs if inp[i] == to_match]
        inputs = new_inputs
        if len(inputs) == 1:
            return inputs[0]
    return inputs[0]


def part1(inputs: list[str]) -> None:
    gamma = "".join([Counter(col).most_common(1)[0][0]for col in get_columns(inputs)])
    epsilon = "".join([str(int(not_(int(s)))) for s in gamma])
    print("gamma  ", gamma)
    print("epsilon", epsilon)
    print("solution part 1:", int(gamma, 2) * int(epsilon, 2))


def part2(inputs):
    oxy = apply_criterion(inputs, criterion="oxy")
    co2 = apply_criterion(inputs, criterion="co2")
    print("solution part 2:", int(oxy, 2) * int(co2, 2))


if __name__ == "__main__":
    inputs = load_inputs("./inputs.txt")
    part1(inputs)
    print("----------")
    part2(inputs)
