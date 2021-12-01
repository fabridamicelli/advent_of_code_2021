from typing import Iterable

from more_itertools import sliding_window, pairwise

from inputs import measurements, example


def n_larger_than_previous(measurements: Iterable[int]) -> int:
    return sum(j > i for i, j in zip(measurements, measurements[1:]))


def n_larger_than_previous_pairwise(measurements: Iterable[int]) -> int:
    return sum(j > i for i, j in pairwise(measurements))


def n_larger_than_previous_sliding(measurements: Iterable[int]) -> int:
    result = []
    previous = sum(measurements[:3])
    for i, _ in enumerate(measurements[:-3], start=1):
        result.append((current := sum(measurements[i:i+3])) > previous)
        previous = current
    return sum(result)


def n_larger_than_previous_sliding_itertools(measurements: Iterable[int]) -> int:
    """Same as n_larger_than_previous_sliding but using more_itertools"""
    windows = sliding_window(measurements, 3)
    previous = sum(next(windows))
    result = []
    for window in windows:
        current = sum(window)
        result.append(current > previous)
        previous = current
    return sum(result)


# Part 1
print("solution part 1:", n_larger_than_previous(measurements))
print("solution part 1:", n_larger_than_previous_pairwise(measurements))


# Part 2
print("solution part 2 -example:", n_larger_than_previous_sliding(example))
print("solution part 2:", n_larger_than_previous_sliding(measurements))
print("solution part 2:", n_larger_than_previous_sliding_itertools(measurements))
