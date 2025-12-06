# Advent of Code 2025, Day 6
# https://adventofcode.com/2025/day/06
from math import prod


fn = {"+": sum, "*": prod}


# Part One
def load_data_1(input_file: str):
    data = open(input_file).read().strip().split("\n")
    table = (line.split() for line in data)
    return zip(*table)


def part_1(input_file):
    data = load_data_1(input_file)
    entries = ((fn[opp], map(int, values)) for *values, opp in data)
    return sum(f(values) for f, values in entries)


# Part Two
def load_data_2(input_file: str):
    data = (line for line in open(input_file).read().split("\n") if line.strip())
    return list(zip(*data))


def part_2(input_file):
    data = load_data_2(input_file)

    entries = []
    for *chars, opp in data:
        line = "".join(chars).strip()
        if not line:
            continue
        if opp.strip():
            entries.append((fn[opp], []))
        entries[-1][1].append(int(line))

    return sum(f(values) for f, values in entries)


if __name__ == "__main__":
    from utils import download_puzzle_input, run

    download_puzzle_input()
    run(part_1, "data/day06-example.txt", expected=4277556)
    run(part_1, "data/day06-data.txt", expected=6757749566978)
    run(part_2, "data/day06-example.txt", expected=3263827)
    run(part_2, "data/day06-data.txt", expected=10603075273949)
