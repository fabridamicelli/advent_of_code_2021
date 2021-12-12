from collections import Counter, defaultdict


def load_inputs(filename):
    with open(filename) as file:
        return list(map(int, file.read().strip().split(",")))


def update_count(count):
    new_count = {}
    new_count[6] = count[0] + count[7]  # reset + previous
    new_count[8] = count[0]  # offspring
    for k in range(1, 9):
        if k == 7:
            continue
        new_count[k-1] = count[k]
    return new_count


def solve():
    count = defaultdict(int, Counter(load_inputs("inputs.txt")))
    for t in range(256):
        if t == 80:
            print("Solution part 1:", sum(count.values()))
        count = update_count(count)
    print("Solution part 2:", sum(count.values()))


solve()
