#!/usr/bin/env python3


def get_val(puzzle: list[list[str]], x: int, y: int) -> str:
    if 0 <= y < len(puzzle) and 0 <= x < len(puzzle[y]):
        return puzzle[y][x]
    return ""


def xmas_matches(puzzle: list[list[str]], x: int, y: int) -> dict[str, bool]:
    xmas = ["X", "M", "A", "S"]
    directions = {
        "→": [get_val(puzzle, x + i, y) for i in range(4)] == xmas,
        "←": [get_val(puzzle, x - i, y) for i in range(4)] == xmas,
        "↓": [get_val(puzzle, x, y + i) for i in range(4)] == xmas,
        "↑": [get_val(puzzle, x, y - i) for i in range(4)] == xmas,
        "↘": [get_val(puzzle, x + i, y + i) for i in range(4)] == xmas,
        "↖": [get_val(puzzle, x - i, y - i) for i in range(4)] == xmas,
        "↙": [get_val(puzzle, x - i, y + i) for i in range(4)] == xmas,
        "↗": [get_val(puzzle, x + i, y - i) for i in range(4)] == xmas,
    }
    return {key: value for key, value in directions.items() if value}


def part1(puzzle: list[list[str]]) -> int:
    n = 0
    for y in range(len(puzzle)):
        for x in range(len(puzzle[y])):
            if puzzle[y][x] == "X":
                n += sum([1 for m in xmas_matches(puzzle, x, y).values() if m])
    return n


def x_mas_matches(puzzle: list[list[str]], x: int, y: int) -> bool:
    x_mas = (
        ("M", "S", "M", "S"),
        ("M", "M", "S", "S"),
        ("S", "M", "S", "M"),
        ("S", "S", "M", "M"),
    )
    neighbours = (
        get_val(puzzle, x - 1, y - 1),  # top left
        get_val(puzzle, x + 1, y - 1),  # top right
        get_val(puzzle, x - 1, y + 1),  # bottom left
        get_val(puzzle, x + 1, y + 1),  # bottom right
    )
    return neighbours in x_mas


def part2(puzzle: list[list[str]]) -> int:
    n = 0
    for y in range(len(puzzle)):
        for x in range(len(puzzle[y])):
            if puzzle[y][x] == "A" and x_mas_matches(puzzle, x, y):
                n += 1
    return n


def read_input() -> list[list[str]]:
    with open("input") as f:
        return [list(line.strip("\n")) for line in f]


if __name__ == "__main__":
    print("Part 1:", part1(read_input()))
    print("Part 2:", part2(read_input()))
