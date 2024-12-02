#!/usr/bin/env python3
from collections.abc import Generator, Iterable
from itertools import pairwise


def increasing(level: Iterable[int]) -> Generator[bool, None, None]:
    return (a < b for a, b in pairwise(level))


def decreasing(level: Iterable[int]) -> Generator[bool, None, None]:
    return (a > b for a, b in pairwise(level))


def safe(level: Iterable[int]) -> Generator[bool, None, None]:
    return (x >= 1 and x <= 3 for x in [abs(a - b) for a, b in pairwise(level)])


def is_safe(level: Iterable[int]) -> bool:
    level = list(level)
    return all(safe(level)) and (all(increasing(level)) or all(decreasing(level)))


def get_level_candidates(level: list[int], index: int) -> tuple[list[int], list[int]]:
    new_level_a = level.copy()
    del new_level_a[index]
    new_level_b = level.copy()
    del new_level_b[index + 1]
    return new_level_a, new_level_b


def is_less_safe(level: list[int]) -> bool:
    left, right = level, level
    if not all(safe(level)):
        left, right = get_level_candidates(level, list(safe(level)).index(False))
        return is_safe(left) or is_safe(right)
    if not all(increasing(level)) and list(increasing(level)).count(False) == 1:
        left, right = get_level_candidates(level, list(increasing(level)).index(False))
        return is_safe(left) or is_safe(right)
    if not all(decreasing(level)) and list(decreasing(level)).count(False) == 1:
        left, right = get_level_candidates(level, list(decreasing(level)).index(False))
        return is_safe(left) or is_safe(right)
    return is_safe(level)


def is_tolerable(level: Iterable[int]) -> bool:
    level = list(level)
    return is_less_safe(level)


def part1(lines: list[Iterable[int]]) -> int:
    return sum(map(is_safe, lines))


def part2(lines: list[Iterable[int]]) -> int:
    return sum(map(is_tolerable, lines))


def read_input() -> list[Iterable[int]]:
    with open("input") as f:
        return [map(int, line.split()) for line in f.read().splitlines()]


if __name__ == "__main__":
    print("Part 1:", part1(read_input()))
    print("Part 2:", part2(read_input()))
