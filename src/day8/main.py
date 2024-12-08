#!/usr/bin/env python3
from collections import defaultdict
from collections.abc import Iterator
from itertools import combinations

X = int
Y = int
Frequency = str
Antenna = tuple[X, Y]
Antennas = dict[Frequency, list[Antenna]]
Antinode = tuple[X, Y]
Harmonic = tuple[X, Y]

Width = int
Height = int
Map = tuple[Width, Height, Antennas]


def get_antinodes(ant1: Antenna, ant2: Antenna) -> tuple[Antinode, Antinode]:
    dx = ant2[0] - ant1[0]
    dy = ant2[1] - ant1[1]
    return (ant1[0] - dx, ant1[1] - dy), (ant2[0] + dx, ant2[1] + dy)


def part1(map: Map) -> int:
    width, height, antennas = map
    antinodes: list[Antinode] = []
    for points in antennas.values():
        for ant1, ant2 in combinations(points, 2):
            for node in get_antinodes(ant1, ant2):
                if 0 <= node[0] < width and 0 <= node[1] < height:
                    antinodes.append(node)
    return len(set(antinodes))


def get_harmonics(
    ant1: Antenna, ant2: Antenna, width: Width, height: Height
) -> Iterator[Harmonic]:
    dx = ant2[0] - ant1[0]
    dy = ant2[1] - ant1[1]
    x, y = ant1
    while (
        (harmonic := (x + dx, y + dy))
        and 0 <= harmonic[0] < width
        and 0 <= harmonic[1] < height
    ):
        yield harmonic
        x += dx
        y += dy
    while (
        (harmonic := (x - dx, y - dy))
        and 0 <= harmonic[0] < width
        and 0 <= harmonic[1] < height
    ):
        yield harmonic
        x -= dx
        y -= dy


def part2(map: Map) -> int:
    width, height, antennas = map
    harmonics: list[Harmonic] = []
    for points in antennas.values():
        for ant1, ant2 in combinations(points, 2):
            harmonics.extend((ant1, ant2))
            for node in get_harmonics(ant1, ant2, width, height):
                harmonics.append(node)
    return len(set(harmonics))


def read_input() -> Map:
    antennas = defaultdict(list)
    with open("input", "r") as f:
        pos = f.tell()
        first_line = f.readline()
        width = len(first_line.rstrip("\n"))
        height = 1 + sum(1 for _ in f)
        f.seek(pos)
        for y, row in enumerate(f.read().splitlines()):
            for x, cell in enumerate(row):
                if cell not in (".", "#"):
                    antennas[cell].append((x, y))
    return (width, height, antennas)


if __name__ == "__main__":
    print("Part 1:", part1(read_input()))
    print("Part 2:", part2(read_input()))
