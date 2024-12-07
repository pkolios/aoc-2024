#!/usr/bin/env python3
from collections.abc import Sequence
from collections import defaultdict, deque
from itertools import takewhile, dropwhile


def check_update(rule_book: dict[int, list[int]], update: Sequence[int]) -> bool:
    for page in update:
        page_rules = rule_book.get(page, [])
        head = update[: update.index(page)]
        for rule in page_rules:
            if rule in head:
                return False
    return True


def get_middle_page(update: Sequence[int]) -> int:
    return update[len(update) // 2]


def get_rule_book(rules: Sequence[tuple[int, ...]]) -> dict[int, list[int]]:
    rule_book = defaultdict(list)
    for key, value in rules:
        rule_book[key].append(value)
    return rule_book


def part1(rules: Sequence[tuple[int, ...]], updates: Sequence[tuple[int, ...]]) -> int:
    rule_book = get_rule_book(rules)
    for key, value in rules:
        rule_book[key].append(value)
    return sum(
        [
            get_middle_page(update)
            for update in updates
            if check_update(rule_book, update)
        ]
    )


def sort_update(rule_book: dict[int, list[int]], update: list[int]) -> list[int]:
    # Step 1: Filter the rule_book to only include numbers in update
    filtered_rule_book = {
        key: [value for value in values if value in update]
        for key, values in rule_book.items()
        if key in update
    }

    # Step 2: Create a graph representation and in-degree dictionary
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    # Step 3: Populate the graph and in-degree based on filtered_rule_book
    for key, values in filtered_rule_book.items():
        for value in values:
            graph[key].append(value)
            in_degree[value] += 1

    # Ensure all nodes in update are in in_degree, even if they have no dependencies
    for num in update:
        if num not in in_degree:
            in_degree[num] = 0

    # Step 4: Perform topological sort
    queue = deque([node for node in update if in_degree[node] == 0])
    sorted_update = []

    while queue:
        node = queue.popleft()
        sorted_update.append(node)

        # Decrease the in-degree of neighbors
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Add any remaining nodes that were not processed (shouldn't happen if no cycles)
    for node in update:
        if node not in sorted_update:
            sorted_update.append(node)

    return sorted_update


def part2(rules: Sequence[tuple[int, ...]], updates: Sequence[tuple[int, ...]]) -> int:
    rule_book = get_rule_book(rules)

    return sum(
        [
            get_middle_page(sort_update(rule_book, list(update)))
            for update in updates
            if not check_update(rule_book, update)
        ]
    )


def read_input() -> tuple[Sequence[tuple[int, ...]], Sequence[tuple[int, ...]]]:
    with open("input") as f:
        lines = [line.strip() for line in f.readlines()]

    rules = [
        tuple(map(int, i.split("|")))
        for i in (takewhile(lambda line: line.strip() != "", lines))
    ]
    updates = [
        tuple(map(int, i.split(",")))
        for i in (dropwhile(lambda line: line.strip() != "", lines))
        if i.strip() != ""
    ]
    return rules, updates


if __name__ == "__main__":
    print("Part 1:", part1(*read_input()))
    print("Part 2:", part2(*read_input()))
