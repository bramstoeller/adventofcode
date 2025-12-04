# Advent of Code 2025, Day 1
# https://adventofcode.com/2025/day/1


def load_data(input_file: str):
    return open(input_file).read().strip().split("\n")


# Part One
def part_1(input_file):
    data = load_data(input_file)
    pos = 50
    at0 = 0
    for line in data:
        delta = int(line[1:]) if line[0] == "R" else -int(line[1:])
        pos = (pos + delta) % 100
        if pos == 0:
            at0 += 1
    return at0


# Part Two
def part_2(input_file):
    data = load_data(input_file)
    pos = 50
    cross0 = 0
    at0 = 0
    for line in data:
        direction = 1 if line[0] == "R" else -1
        delta = int(line[1:])
        full_turns = delta // 100
        rest = delta % 100
        cross0 += full_turns
        pos += direction * rest
        if not (pos - direction * rest) % 100 or not pos % 100:
            block = True
        else:
            block = False
        if pos < 0:
            pos += 100
            if not block:
                cross0 += 1
        if pos >= 100:
            pos -= 100
            if not block:
                cross0 += 1
        if pos == 0:
            at0 += 1
    return cross0 + at0


def part_2_optimized(input_file):
    data = load_data(input_file)
    pos = 50
    hit0 = 0
    for i, line in enumerate(data):
        cw = line[0] == "R"
        delta = int(line[1:])
        pos = (pos if cw else 100 - pos) % 100 + delta
        hit0 += pos // 100
        pos = (pos if cw else 100 - pos) % 100
    return hit0


if __name__ == "__main__":
    from utils import run

    run(part_1, "data/day01-example.txt", expected=3)
    run(part_1, "data/day01-data.txt", expected=1177)
    run(part_2, "data/day01-example.txt", expected=6)
    run(part_2, "data/day01-data.txt", expected=6768)
    run(part_2_optimized, "data/day01-example.txt", expected=6)
    run(part_2_optimized, "data/day01-data.txt", expected=6768)
