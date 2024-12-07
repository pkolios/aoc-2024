#!/usr/bin/env python3

from collections.abc import Callable, Iterable
from itertools import product
import operator as op


type TestValue = int
type Numbers = list[int]
type Equation = tuple[TestValue, Numbers]


def can_be_combined(equation: Equation, ops: Iterable[Callable]) -> bool:
    test, nums = equation
    for operations in product(ops, repeat=len(nums) - 1):
        result = nums[0]
        for i, op_ in enumerate(operations):
            result = op_(result, nums[i + 1])
            if result > test:
                break
        if result == test:
            return True
    return False


def part1(equations: list[Equation]) -> int:
    return sum(eq[0] for eq in equations if can_be_combined(eq, (op.add, op.mul)))


def concat(a: int, b: int) -> int:
    return int(str(a) + str(b))


def part2(equations: list[Equation]) -> int:
    return sum(
        eq[0] for eq in equations if can_be_combined(eq, (op.add, op.mul, concat))
    )


def read_input() -> list[Equation]:
    with open("input") as f:
        return [
            (int(test), list(map(int, nums.split())))
            for line in f.read().splitlines()
            for test, nums in [line.split(":")]
        ]


if __name__ == "__main__":
    print("Part 1:", part1(read_input()))
    print("Part 2:", part2(read_input()))
