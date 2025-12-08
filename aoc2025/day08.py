# Advent of Code 2025, Day 8
# https://adventofcode.com/2025/day/8

from dataclasses import dataclass
from math import prod


@dataclass
class Box:
    x: int
    y: int
    z: int


def load_data(input_file: str):
    return [Box(*map(int, line.split(","))) for line in open(input_file).read().strip().split("\n")]


def square_distance(a: Box, b: Box):
    dx = b.x - a.x
    dy = b.y - a.y
    dz = b.z - a.z
    return dx * dx + dy * dy + dz * dz


def all_distances(boxes):
    return {(i, j): square_distance(a, b) for i, a in enumerate(boxes) for j, b in enumerate(boxes) if i < j}


def sort_distances(distances: dict[tuple[int, int], float]):
    return [idx for idx, _ in sorted(distances.items(), key=lambda x: x[1])]


def merge(groups: list[set], new_group: set):
    linked = [i for i, m in enumerate(groups) if m & new_group]
    if not linked:
        groups.append(new_group)
        return groups
    first = linked[0]
    rest = linked[1:]
    groups[first] |= new_group
    for i in rest:
        groups[first] |= groups[i]
    return groups[: first + 1] + [m for m in groups[first + 1 :] if not m & new_group]


# Part One
def part_1(input_file: str, n: int, m: int = 3):
    boxes = load_data(input_file)
    distances = all_distances(boxes)
    sorted_edges = sort_distances(distances)
    circuits: list[set[int]] = []
    for a, b in sorted_edges[:n]:
        circuits = merge(circuits, {a, b})
    circuit_sizes = list(reversed(sorted(len(c) for c in circuits)))
    return prod(circuit_sizes[:m])


# Part Two
def part_2(input_file: str):
    boxes = load_data(input_file)
    distances = all_distances(boxes)
    sorted_edges = sort_distances(distances)
    N = len(boxes)
    circuits: list[set[int]] = []
    for a, b in sorted_edges:
        circuits = merge(circuits, {a, b})
        if len(circuits) == 1 and len(circuits[0]) == N:
            return boxes[a].x * boxes[b].x
    return None


if __name__ == "__main__":
    from utils import download_puzzle_input, run

    download_puzzle_input()
    run(part_1, "data/day08-example.txt", n=10, expected=40)
    run(part_1, "data/day08-data.txt", n=1000, expected=72150)
    run(part_2, "data/day08-example.txt", expected=25272)
    run(part_2, "data/day08-data.txt", expected=3926518899)
