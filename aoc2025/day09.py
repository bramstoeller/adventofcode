# Advent of Code 2025, Day 9
# https://adventofcode.com/2025/day/9
from bisect import bisect
from dataclasses import dataclass


@dataclass
class Tile:
    x: int
    y: int


def load_data(input_file: str):
    return [Tile(*map(int, line.split(","))) for line in open(input_file).read().strip().split("\n")]


def area(a: Tile, b: Tile):
    dx = abs(b.x - a.x) + 1
    dy = abs(b.y - a.y) + 1
    return dx * dy


# Part One
def part_1(input_file):
    tiles = load_data(input_file)
    rectangles = ((a, b) for i, a in enumerate(tiles) for b in tiles[i + 1 :])
    return max(area(*rect) for rect in rectangles)


# Part Two
def sorted_edges(vertices):
    edges = list(zip(vertices, vertices[1:] + vertices[:1]))
    vertical = ((a.x, min(a.y, b.y), max(a.y, b.y)) for a, b in edges if a.x == b.x)
    horizontal = ((a.y, min(a.x, b.x), max(a.x, b.x)) for a, b in edges if a.y == b.y)
    return sorted(vertical), sorted(horizontal)


def intersect_any_edges(p0, p1, vertical, horizontal):
    x0, x1 = min(p0.x, p1.x), max(p0.x, p1.x)
    y0, y1 = min(p0.y, p1.y), max(p0.y, p1.y)

    lower_bound = bisect(vertical, (x0 + 1,))
    upper_bound = bisect(vertical, (x1,))
    for _, edge_y_min, edge_y_max in vertical[lower_bound:upper_bound]:
        if edge_y_min < y1 and edge_y_max > y0:
            return True

    lower_bound = bisect(horizontal, (y0 + 1,))
    upper_bound = bisect(horizontal, (y1,))
    for _, edge_x_min, edge_x_max in horizontal[lower_bound:upper_bound]:
        if edge_x_min < x1 and edge_x_max > x0:
            return True

    return False


def part_2(input_file):
    tiles = load_data(input_file)
    vertical, horizontal = sorted_edges(tiles)

    rectangles = ((a, b) for i, a in enumerate(tiles) for b in tiles[i + 1 :])
    rectangles = sorted(rectangles, key=lambda rect: area(*rect), reverse=True)

    for p0, p1 in rectangles:
        if not intersect_any_edges(p0, p1, vertical, horizontal):
            return area(p0, p1)

    return None


if __name__ == "__main__":
    from utils import download_puzzle_input, run

    download_puzzle_input()
    run(part_1, "data/day09-example.txt", expected=50)
    run(part_1, "data/day09-data.txt", expected=4746238001)
    run(part_2, "data/day09-example.txt", expected=24)
    run(part_2, "data/day09-data.txt", expected=1552139370)
