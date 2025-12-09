# Advent of Code 2025, Day 9
# https://adventofcode.com/2025/day/9
from dataclasses import dataclass


@dataclass
class Node:
    x: int
    y: int


def load_data(input_file: str):
    return [Node(*map(int, line.split(","))) for line in open(input_file).read().strip().split("\n")]


def area(a: Node, b: Node):
    dx = abs(b.x - a.x) + 1
    dy = abs(b.y - a.y) + 1
    return dx * dy


def sorted_rectangles(boxes):
    return sorted(
        ((i, j) for i in range(len(boxes)) for j in range(i + 1, len(boxes))),
        key=lambda pair: area(boxes[pair[0]], boxes[pair[1]]),
    )


# Part One
def part_1(input_file):
    boxes = load_data(input_file)
    connections = sorted_rectangles(boxes)
    pair = connections[-1]
    return area(boxes[pair[0]], boxes[pair[1]])


# Part Two


def node_in_polygon(p, vertices) -> bool:
    n = len(vertices)

    def edges():
        return ((vertices[i], vertices[(i + 1) % n]) for i in range(n))

    def between(a: int, b: int, v: int) -> bool:
        return a <= v <= b if a <= b else b <= v <= a

    def on_edge(p: Node, a: Node, b: Node) -> bool:
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


def in_polygon(a: Node, b: Node, boxes) -> bool:
    x0, x1 = min(a.x, b.x), max(a.x, b.x)
    y0, y1 = min(a.y, b.y), max(a.y, b.y)

    corners = [Node(x0, y0), Node(x1, y0), Node(x1, y1), Node(x0, y1)]
    for p in corners:
        if not node_in_polygon(p, boxes):
            return False

    for d in [10001, 1001, 101, 11, 1]:
        for x in range(x0, x1 + 1, d):
            p0 = Node(x, y0)
            p1 = Node(x, y1)
            if not node_in_polygon(p0, boxes) or not node_in_polygon(p1, boxes):
                return False

        for y in range(y0, y1 + 1, d):
            p0 = Node(x0, y)
            p1 = Node(x0, y)
            if not node_in_polygon(p0, boxes) or not node_in_polygon(p1, boxes):
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
    boxes = load_data(input_file)
    connections = reversed(sorted_rectangles(boxes))
    for connection in connections:
        if in_polygon(boxes[connection[0]], boxes[connection[1]], boxes):
            plot_polygon(boxes[connection[0]], boxes[connection[1]], boxes)
            return area(boxes[connection[0]], boxes[connection[1]])


if __name__ == "__main__":
    from utils import download_puzzle_input, run

    download_puzzle_input()
    run(part_1, "data/day09-example.txt", expected=50)
    run(part_1, "data/day09-data.txt")
    run(part_2, "data/day09-example.txt", expected=24)
    run(part_2, "data/day09-data.txt")
