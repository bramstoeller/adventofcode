# Advent of Code 2024, Day 19
# https://adventofcode.com/2024/day/19
from functools import cache


# Part One
def load_data(file_name):
    data = open(file_name, "r").read()
    towels, patterns = data.split("\n\n")
    towels = list(towels.strip().split(", "))
    patterns = [line.strip() for line in patterns.strip().split("\n")]
    return towels, patterns


@cache
def has_design(pattern, towels):
    if len(pattern) == 0:
        return True
    return any(has_design(pattern[len(t):], towels) for t in towels if pattern.startswith(t))


def part_1(file_name):
    towels, patterns = load_data(file_name)
    return sum(has_design(p, tuple(towels)) for p in patterns)


# Part Two

@cache
def count_designs(pattern, towels):
    if len(pattern) == 0:
        return 1
    return sum(count_designs(pattern[len(t):], towels) for t in towels if pattern.startswith(t))


def part_2(file_name):
    towels, patterns = load_data(file_name)
    return sum(count_designs(p, tuple(towels)) for p in patterns)


if __name__ == "__main__":
    from utils import run

    run(part_1, "data/day19-example.txt", expected=6)
    run(part_1, "data/day19-data.txt", )
    run(part_2, "data/day19-example.txt", expected=16)
    run(part_2, "data/day19-data.txt")
