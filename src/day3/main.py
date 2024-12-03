#!/usr/bin/env python3
import re


def part1(program: str) -> int:
    instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)", program)
    return sum(
        [int(a) * int(b) for a, b in [re.findall(r"\d+", i) for i in instructions]]
    )


def part2(program: str) -> int:
    matches = re.findall(r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))", program)
    instructions = []
    enabled = True
    for item in matches:
        match item:
            case "do()":
                enabled = True
            case "don't()":
                enabled = False
            case _:
                if enabled:
                    instructions.append(item)
    return sum(
        [int(a) * int(b) for a, b in [re.findall(r"\d+", i) for i in instructions]]
    )


def read_input() -> str:
    with open("input") as f:
        return f.read()


if __name__ == "__main__":
    print("Part 1:", part1(read_input()))
    print("Part 2:", part2(read_input()))
