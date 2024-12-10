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
        paths = [p + [p[-1] + d] for p in paths for d in (1j ** i for i in range(4)) if p[-1] + d in nodes[h]]
    return paths


def part_1(file_name):
    return len(set((p[0], p[-1]) for p in plan_routes(load_data(file_name))))


# Part Two
def part_2(file_name):
    return len(plan_routes(load_data(file_name)))


if __name__ == "__main__":
    print("1. Example 1.1:", part_1("data/day10-example1-1.txt"), "=? 1")
    print("1. Example 1.2:", part_1("data/day10-example1-2.txt"), "=? 2")
    print("1. Example 1.3:", part_1("data/day10-example1-3.txt"), "=? 4")
    print("1. Example 1.4:", part_1("data/day10-example1-4.txt"), "=? 3")
    print("1. Example 1.5:", part_1("data/day10-example1-5.txt"), "=? 36")
    print("1. Answer:", part_1("data/day10-data.txt"))

    print("2. Example 2.1:", part_2("data/day10-example2-1.txt"), "=? 3")
    print("2. Example 2.2:", part_2("data/day10-example2-2.txt"), "=? 13")
    print("2. Example 2.3:", part_2("data/day10-example2-3.txt"), "=? 81")
    print("2. Answer:", part_2("data/day10-data.txt"))
