#!/usr/bin/env python3
import operator
from itertools import starmap
from collections.abc import Iterable
from collections import Counter


def part1(lines: list[Iterable[int]]) -> int:
    return sum(map(abs, starmap(operator.sub, zip(*map(sorted, zip(*lines))))))


def part2(lines: list[Iterable[int]]) -> int:
    left, right = zip(*lines)
    left_counter, right_counter = Counter(left), Counter(right)
    return sum(num * count * right_counter[num] for num, count in left_counter.items())


def read_input() -> list[Iterable[int]]:
    with open("input") as f:
        return [map(int, line.split()) for line in f.read().splitlines()]


if __name__ == "__main__":
    print("Part 1:", part1(read_input()))
    print("Part 2:", part2(read_input()))
