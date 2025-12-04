# Advent of Code 2025, Day 0
# https://adventofcode.com/2025/day/0


def load_data(input_file: str):
    return open(input_file).read().strip().split("\n")


# Part One
def part_1(input_file):
    _data = load_data(input_file)
    return 0


# Part Two
def part_2(input_file):
    _data = load_data(input_file)
    return 0


if __name__ == "__main__":
    from utils import run

    run(part_1, "data/day00-example.txt", expected=0)
    run(part_1, "data/day00-data.txt")
    run(part_2, "data/day00-example.txt", expected=0)
    run(part_2, "data/day00-data.txt")
