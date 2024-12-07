#!/usr/bin/env python3


def in_bounds(
    grid: list[list[str]],
    x: int,
    y: int,
) -> bool:
    return 0 <= y < len(grid) and 0 <= x < len(grid[y])


def next_pos(
    grid: list[list[str]],
    x: int,
    y: int,
    direction: str,
) -> tuple[int, int, str] | None:
    ny, nx = y, x
    match direction:
        case "^":
            ny -= 1
        case "v":
            ny += 1
        case "<":
            nx -= 1
        case ">":
            nx += 1
        case _:
            raise ValueError(f"Invalid direction: {direction}")
    if not in_bounds(grid, nx, ny):
        return None
    # Rotate if next position is an obstacle
    if grid[ny][nx] == "#":
        match direction:
            case "^":
                return next_pos(grid, x, y, ">")
            case "v":
                return next_pos(grid, x, y, "<")
            case "<":
                return next_pos(grid, x, y, "^")
            case ">":
                return next_pos(grid, x, y, "v")
            case _:
                raise ValueError(f"Invalid direction: {direction}")
    return nx, ny, direction


def find_starting_position(grid: list[list[str]]) -> tuple[int, int, str]:
    for i, row in enumerate(grid):
        if "^" in row:
            return row.index("^"), i, "^"
    else:
        raise ValueError("No starting position found")


def X_marks_the_spot(grid: list[list[str]]) -> list[list[str]]:
    x, y, direction = find_starting_position(grid)
    grid[y][x] = "X"
    while (new_pos := next_pos(grid, x, y, direction)) is not None:
        x, y, direction = new_pos
        grid[y][x] = "X"
    return grid


def part1(grid: list[list[str]]) -> int:
    grid = X_marks_the_spot(grid)
    return sum([row.count("X") for row in grid])


def simulate_with_obstacle(
    original_grid: list[list[str]], sx: int, sy: int, direction: str, ox: int, oy: int
) -> bool:
    grid = [row[:] for row in original_grid]
    # Place the new obstacle
    grid[oy][ox] = "#"

    visited_states = set()
    x, y = sx, sy
    state = (x, y, direction)
    while True:
        if state in visited_states:
            return True
        visited_states.add(state)

        next_state = next_pos(grid, x, y, direction)
        if next_state is None:
            return False
        x, y, direction = next_state
        state = (x, y, direction)


def part2(grid: list[list[str]]) -> int:
    sx, sy, direction = find_starting_position(grid)
    grid = X_marks_the_spot(grid)

    possible_positions = []
    for ry, row in enumerate(grid):
        for rx, val in enumerate(row):
            if val == "X" and not (rx == sx and ry == sy):
                possible_positions.append((rx, ry))

    count = 0
    for ox, oy in possible_positions:
        if simulate_with_obstacle(grid, sx, sy, direction, ox, oy):
            count += 1

    return count


def read_input() -> list[list[str]]:
    with open("input") as f:
        return [list(line.strip("\n")) for line in f]


if __name__ == "__main__":
    print("Part 1:", part1(read_input()))
    print("Part 2:", part2(read_input()))
