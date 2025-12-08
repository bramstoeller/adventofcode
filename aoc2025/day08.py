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


def sorted_connection(boxes):
    return sorted(
        ((i, j) for i in range(len(boxes)) for j in range(i + 1, len(boxes))),
        key=lambda pair: square_distance(boxes[pair[0]], boxes[pair[1]]),
    )


def merge(circuits: list[set], connection: set):
    linked = [m for m in circuits if m & connection]
    if not linked:
        circuits.append(connection)
        return circuits
    linked[0] |= connection
    if len(linked) > 1:
        linked[0] |= linked[1]
        circuits.remove(linked[1])
    return circuits


# Part One
def part_1(input_file: str, n: int, m: int = 3):
    boxes = load_data(input_file)
    connections = sorted_connection(boxes)
    circuits: list[set[int]] = []
    for a, b in connections[:n]:
        circuits = merge(circuits, {a, b})
    circuit_sizes = list(reversed(sorted(len(c) for c in circuits)))
    return prod(circuit_sizes[:m])


# Part Two
def part_2(input_file: str):
    boxes = load_data(input_file)
    connections = sorted_connection(boxes)
    N = len(boxes)
    circuits: list[set[int]] = []
    for a, b in connections:
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
