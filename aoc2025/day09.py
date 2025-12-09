# Advent of Code 2025, Day 9
# https://adventofcode.com/2025/day/9
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
def intersect_any_edges(p0, p1, horizontal, vertical):
    x0, x1 = min(p0.x, p1.x), max(p0.x, p1.x)
    y0, y1 = min(p0.y, p1.y), max(p0.y, p1.y)
    for x, y_min, y_max in vertical:
        if x0 < x < x1 and y1 > y_min and y0 < y_max:
            return True
    for y, x_min, x_max in horizontal:
        if y0 < y < y1 and x1 > x_min and x0 < x_max:
            return True
    return False


def part_2(input_file):
    tiles = load_data(input_file)
    edges = list(zip(tiles, tiles[1:] + tiles[:1]))
    horizontal = [(a.y, min(a.x, b.x), max(a.x, b.x)) for a, b in edges if a.y == b.y]
    vertical = [(a.x, min(a.y, b.y), max(a.y, b.y)) for a, b in edges if a.x == b.x]
    rectangles = ((a, b) for i, a in enumerate(tiles) for b in tiles[i + 1 :])
    rectangles = sorted(rectangles, key=lambda rect: area(*rect), reverse=True)
    for p0, p1 in rectangles:
        if not intersect_any_edges(p0, p1, horizontal, vertical):
            return area(p0, p1)
    return None


if __name__ == "__main__":
    from utils import download_puzzle_input, run

    download_puzzle_input()
    run(part_1, "data/day09-example.txt", expected=50)
    run(part_1, "data/day09-data.txt", expected=4746238001)
    run(part_2, "data/day09-example.txt", expected=24)
    run(part_2, "data/day09-data.txt", expected=1552139370)
