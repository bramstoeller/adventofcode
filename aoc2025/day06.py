# Advent of Code 2025, Day 06
# https://adventofcode.com/2025/day/06
from math import prod


# Part One
def load_data_1(input_file: str):
    data = open(input_file).read().strip().split("\n")
    table = (line.split() for line in data)
    transposed = zip(*table)
    return transposed


def part_1(input_file):
    data = load_data_1(input_file)
    entries = ((sum if opp == "+" else prod, map(int, values)) for *values, opp in data)
    return sum(func(values) for func, values in entries)


# Part Two
def load_data_2(input_file: str):
    data = (line for line in open(input_file).read().split("\n") if line.strip())
    transposed = list(zip(*data))
    return transposed


def part_2(input_file):
    data = load_data_2(input_file)

    entries = []
    for *chars, opp in data:
        line = "".join(chars).strip()
        if not line:
            continue
        if opp.strip():
            entries.append((sum if opp == "+" else prod, []))
        entries[-1][1].append(int(line))

    return sum(func(values) for func, values in entries)


if __name__ == "__main__":
    from utils import download_puzzle_input, run

    download_puzzle_input()
    run(part_1, "data/day06-example.txt", expected=4277556)
    run(part_1, "data/day06-data.txt", expected=6757749566978)
    run(part_2, "data/day06-example.txt", expected=3263827)
    run(part_2, "data/day06-data.txt", expected=10603075273949)
