# Advent of Code 2025, Day 8
# https://adventofcode.com/2025/day/8

from dataclasses import dataclass
from math import sqrt


@dataclass
class Node:
    x: int
    y: int
    z: int


def load_data(input_file: str):
    return [Node(*map(int, line.split(","))) for line in open(input_file).read().strip().split("\n")]


def all_distances(nodes):
    return {(i, j): manhattan_distance(a, b) for i, a in enumerate(nodes) for j, b in enumerate(nodes) if i < j}


def manhattan_distance(a: Node, b: Node):
    dx = b.x - a.x
    dy = b.y - a.y
    dz = b.z - a.z
    return sqrt(dx * dx + dy * dy + dz * dz)


def sort_distances(distances):
    return [idx for idx, _ in sorted(distances.items(), key=lambda x: x[1])]


def get_neighbors(node, edges):
    return [a if b == node else b for a, b in edges if a == node or b == node]


def find_path(start, goal, nodes, edges):
    open_set = {start}
    closed_set = set()
    g = {start: 0.0}
    f = {start: manhattan_distance(nodes[start], nodes[goal])}

    while open_set:
        current = min(open_set, key=lambda x: f[x])
        if current == goal:
            return True
        open_set.remove(current)
        closed_set.add(current)
        nbh = get_neighbors(current, edges)
        for nb in nbh:
            g_score = g[current] + manhattan_distance(nodes[current], nodes[nb])
            if nb in closed_set:
                continue
            if nb not in open_set:
                open_set.add(nb)
            elif g_score >= g[nb]:
                continue
            g[nb] = g_score
            f[nb] = g_score + manhattan_distance(nodes[nb], nodes[goal])
    return False


def merge(groups):
    merged = []
    for g in groups:
        linked = [i for i, m in enumerate(merged) if g & m]
        if not linked:
            merged.append(g)
            continue
        first = linked[0]
        rest = linked[1:]
        merged[first] |= g
        for i in rest:
            merged[first] |= merged[i]
        merged = merged[: first + 1] + [m for m in merged[first + 1 :] if not g & m]
    return merged


# Part One
def part_1(input_file, n):
    nodes = load_data(input_file)
    distances = all_distances(nodes)
    sorted_edges = sort_distances(distances)
    connected = []
    groups = []
    for a, b in sorted_edges[:n]:
        if not find_path(a, b, nodes, connected):
            connected.append((a, b))
            groups = merge(groups + [{a, b}])

    N = list(reversed(sorted(len(g) for g in groups)))
    return N[0] * N[1] * N[2]


# Part Two
def part_2(input_file):
    nodes = load_data(input_file)
    N = len(nodes)
    distances = all_distances(nodes)
    sorted_edges = sort_distances(distances)
    connected = []
    groups = []
    for a, b in sorted_edges:
        if not find_path(a, b, nodes, connected):
            connected.append((a, b))
            groups = merge(groups + [{a, b}])
        if len(groups) == 1 and len(groups[0]) == N:
            return nodes[a].x * nodes[b].x


if __name__ == "__main__":
    from utils import download_puzzle_input, run

    download_puzzle_input()
    run(part_1, "data/day08-example.txt", n=10, expected=40)
    run(part_1, "data/day08-data.txt", n=1000, expected=72150)
    run(part_2, "data/day08-example.txt", expected=25272)
    run(part_2, "data/day08-data.txt", expected=3926518899)
