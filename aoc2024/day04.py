# Advent of Code 2024, Day 4
# https://adventofcode.com/2024/day/4


# Part One
def load_data(file_name):
    return [line.strip() for line in open(file_name, "r").readlines()]


def find_occurrences(data, needle):
    # Find starting point candidates
    candidates = []
    for y, line in enumerate(data):
        candidates += [(x, y) for x, c in enumerate(line) if c == needle[0]]

    # Check all eight directions
    n = len(needle)
    max_x = len(data[0]) - 1
    max_y = len(data) - 1
    for x, y in candidates:
        for dy in [-1, 0, 1]:
            if y + dy * (n - 1) < 0 or y + dy * (n - 1) > max_y:
                continue
            for dx in [-1, 0, 1]:
                if (dx == 0 and dy == 0) or x + dx * (n - 1) < 0 or x + dx * (n - 1) > max_x:
                    continue
                if all(c == data[y + i * dy][x + i * dx] for i, c in enumerate(needle)):
                    yield x, y, dx, dy


def part_1(file_name):
    needle = "XMAS"
    return len(list(find_occurrences(load_data(file_name), needle)))


# Part Two
def find_occurrences_cross(data, needle):
    # Find starting point candidates
    n = len(needle) // 2
    candidates = []
    for y, line in enumerate(data):
        candidates += [(x, y) for x, c in enumerate(line) if c == needle[n]]

    # Check all four directions
    max_x = len(data[0]) - 1
    max_y = len(data) - 1
    for x, y in candidates:
        found = 0
        for dy in [-1, 1]:
            if y - dy * n < 0 or y + dy * n < 0 or y - dy * n > max_y or y + dy * n > max_y:
                continue
            for dx in [-1, 1]:
                if x - dx * n < 0 or x + dx * n < 0 or x - dx * n > max_x or x + dx * n > max_x:
                    continue
                if all(c == data[y + (i - n) * dy][x + (i - n) * dx] for i, c in enumerate(needle)):
                    found += 1
        if found == 2:
            yield x, y


def part_2(file_name):
    needle = "MAS"
    return len(list(find_occurrences_cross(load_data(file_name), needle)))


if __name__ == "__main__":
    from utils import run

    run(part_1, "data/day04-example.txt", expected=18)
    run(part_1, "data/day04-data.txt", expected=2517)
    run(part_2, "data/day04-example.txt", expected=9)
    run(part_2, "data/day04-data.txt", expected=1960)
