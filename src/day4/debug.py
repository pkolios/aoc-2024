from typing import Callable


def print_part1(
    puzzle: list[list[str]],
    match_func: Callable[[list[list[str]], int, int], dict[str, bool]],
) -> None:
    def set_xmas(
        grid: list[list[str]],
        x: int,
        y: int,
        matches: dict[str, bool],
    ) -> list[list[str]]:
        xmas = ["X", "M", "A", "S"]
        for key, _ in matches.items():
            match key:
                case "→":
                    for i in range(4):
                        grid[y][x + i] = xmas[i]
                case "←":
                    for i in range(4):
                        grid[y][x - i] = xmas[i]
                case "↓":
                    for i in range(4):
                        grid[y + i][x] = xmas[i]
                case "↑":
                    for i in range(4):
                        grid[y - i][x] = xmas[i]
                case "↘":
                    for i in range(4):
                        grid[y + i][x + i] = xmas[i]
                case "↖":
                    for i in range(4):
                        grid[y - i][x - i] = xmas[i]
                case "↙":
                    for i in range(4):
                        grid[y + i][x - i] = xmas[i]
                case "↗":
                    for i in range(4):
                        grid[y - i][x + i] = xmas[i]
                case _:
                    raise ValueError("Invalid direction")
        return grid

    grid = [["." for _ in range(len(puzzle[y]))] for y in range(len(puzzle))]
    for y in range(len(puzzle)):
        for x in range(len(puzzle[y])):
            if puzzle[y][x] == "X":
                matches = match_func(puzzle, x, y)
                grid = set_xmas(grid, x, y, matches)
    grid_str = "\n".join(["".join(row) for row in grid])
    print(grid_str)
