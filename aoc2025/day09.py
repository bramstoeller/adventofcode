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
def node_in_polygon(p, vertices) -> bool:
    n = len(vertices)

    def edges():
        return ((vertices[i], vertices[(i + 1) % n]) for i in range(n))

    def between(a: int, b: int, v: int) -> bool:
        return a <= v <= b if a <= b else b <= v <= a

    def on_edge(p: Tile, a: Tile, b: Tile) -> bool:
        if a.x == b.x:
            return p.x == a.x and between(a.y, b.y, p.y)
        return p.y == a.y and between(a.x, b.x, p.x)

    for a, b in edges():
        if on_edge(p, a, b):
            return True

    inside = False
    x, y = p.x, p.y

    for a, b in edges():
        if a.y == b.y:
            continue
        y_min = min(a.y, b.y)
        y_max = max(a.y, b.y)
        if y_min <= y < y_max:
            if a.x > x:
                inside = not inside

    return inside


def in_polygon(a: Tile, b: Tile, vertices) -> bool:
    x0, x1 = min(a.x, b.x), max(a.x, b.x)
    y0, y1 = min(a.y, b.y), max(a.y, b.y)

    corners = [Tile(x0, y0), Tile(x1, y0), Tile(x1, y1), Tile(x0, y1)]
    for p in corners:
        if not node_in_polygon(p, vertices):
            return False

    for d in [10001, 1001, 101, 11, 1]:
        for x in range(x0, x1 + 1, d):
            p0 = Tile(x, y0)
            p1 = Tile(x, y1)
            if not node_in_polygon(p0, vertices) or not node_in_polygon(p1, vertices):
                return False

        for y in range(y0, y1 + 1, d):
            p0 = Tile(x0, y)
            p1 = Tile(x0, y)
            if not node_in_polygon(p0, vertices) or not node_in_polygon(p1, vertices):
                return False

    return True


def plot_polygon(a, b, boxes):
    import matplotlib.pyplot as plt

    x0, x1 = min(a.x, b.x), max(a.x, b.x)
    y0, y1 = min(a.y, b.y), max(a.y, b.y)

    poly_x = [p.x for p in boxes] + [boxes[0].x]
    poly_y = [p.y for p in boxes] + [boxes[0].y]
    rect_x = [x0, x1, x1, x0, x0]
    rect_y = [y0, y0, y1, y1, y0]

    plt.plot(poly_x, poly_y, "b")
    plt.plot(rect_x, rect_y, "r-")

    plt.grid()
    plt.show()


def part_2(input_file):
    tiles = load_data(input_file)
    rectangles = ((a, b) for i, a in enumerate(tiles) for b in tiles[i + 1 :])
    rectangles = reversed(sorted(rectangles, key=lambda rect: area(*rect)))

    for p0, p1 in rectangles:
        if in_polygon(p0, p1, tiles):
            plot_polygon(p0, p1, tiles)
            return area(p0, p1)


if __name__ == "__main__":
    from utils import download_puzzle_input, run

    download_puzzle_input()
    run(part_1, "data/day09-example.txt", expected=50)
    run(part_1, "data/day09-data.txt", expected=4746238001)
    run(part_2, "data/day09-example.txt", expected=24)
    run(part_2, "data/day09-data.txt", expected=1552139370)
