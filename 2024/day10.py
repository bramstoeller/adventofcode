# Advent of Code 2024, Day 01
# https://adventofcode.com/2024/day/10


# Part One

def load_data(file_name):
    data = open(file_name, "r").readlines()
    return {(x, y): int(h) for y, line in enumerate(data) for x, h in enumerate(line.strip()) if h != "."}


def plan_routes(data):
    paths = [[(x, y)] for (x, y), h in data.items() if h == 0]
    for h in range(1, 10):
        new_paths = []
        for p in paths:
            x, y = p[-1]
            if (x, y - 1) in data and data[(x, y - 1)] == h:
                new_paths.append(p + [(x, y - 1)])
            if (x, y + 1) in data and data[(x, y + 1)] == h:
                new_paths.append(p + [(x, y + 1)])
            if (x - 1, y) in data and data[(x - 1, y)] == h:
                new_paths.append(p + [(x - 1, y)])
            if (x + 1, y) in data and data[(x + 1, y)] == h:
                new_paths.append(p + [(x + 1, y)])
        paths = new_paths
    return paths


def part_1(file_name):
    routes = plan_routes(load_data(file_name))
    endpoints = [p[0] + p[1] for p in routes]
    return len(set(endpoints))


# Part Two
def part_2(file_name):
    routes = plan_routes(load_data(file_name))
    return len(routes)


if __name__ == "__main__":
    print("1. Example 1:", part_1("data/day10-example1-1.txt"), "=? 1")
    print("1. Example 2:", part_1("data/day10-example1-2.txt"), "=? 2")
    print("1. Example 3:", part_1("data/day10-example1-3.txt"), "=? 4")
    print("1. Example 4:", part_1("data/day10-example1-4.txt"), "=? 3")
    print("1. Example 5:", part_1("data/day10-example1-5.txt"), "=? 36")
    print("1. Answer:", part_1("data/day10-data.txt"))

    print("2. Example 1:", part_2("data/day10-example2-1.txt"), "=? 3")
    print("2. Example 2:", part_2("data/day10-example2-2.txt"), "=? 13")
    print("2. Example 3:", part_2("data/day10-example2-3.txt"), "=? 81")
    print("2. Answer:", part_2("data/day10-data.txt"))
