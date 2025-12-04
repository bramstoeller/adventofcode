# Advent of Code 2024, Day 10
# https://adventofcode.com/2024/day/10


# Part One
def load_data(file_name):
    data = enumerate(open(file_name, "r").readlines())
    return [(x, y, h) for y, line in data for x, h in enumerate(line.strip()) if h != "."]


def plan_routes(data):
    nodes = {i: set() for i in range(10)}
    for x, y, h in data:
        nodes[int(h)].add(x + y * 1j)

    paths = [[n] for n in nodes[0]]
    for h in range(1, 10):
        paths = [p + [p[-1] + d] for p in paths for d in (1j**i for i in range(4)) if p[-1] + d in nodes[h]]
    return paths


def part_1(file_name):
    return len(set((p[0], p[-1]) for p in plan_routes(load_data(file_name))))


# Part Two
def part_2(file_name):
    return len(plan_routes(load_data(file_name)))


if __name__ == "__main__":
    from utils import run

    run(part_1, "data/day10-example1-1.txt", expected=1)
    run(part_1, "data/day10-example1-2.txt", expected=2)
    run(part_1, "data/day10-example1-3.txt", expected=4)
    run(part_1, "data/day10-example1-4.txt", expected=3)
    run(part_1, "data/day10-example1-5.txt", expected=36)
    run(part_1, "data/day10-data.txt", expected=688)
    run(part_2, "data/day10-example2-1.txt", expected=3)
    run(part_2, "data/day10-example2-2.txt", expected=13)
    run(part_2, "data/day10-example2-3.txt", expected=81)
    run(part_2, "data/day10-data.txt", expected=1459)
