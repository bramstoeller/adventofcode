# Advent of Code 2025, Day 7
# https://adventofcode.com/2025/day/7
from collections import defaultdict


def load_data(input_file: str):
    return open(input_file).read().strip().split("\n")


# Part One
def part_1(input_file):
    data = load_data(input_file)
    beams = {data[0].index("S")}
    splitted = 0
    for line in data[1:]:
        new_beams = {b for b in beams}
        for b in beams:
            if line[b] == "^":
                new_beams.remove(b)
                splitted += 1
                if b > 1:
                    new_beams.add(b - 1)
                if b < len(line) - 1:
                    new_beams.add(b + 1)
        beams = new_beams

    return splitted


# Part Two
def part_2(input_file):
    data = load_data(input_file)
    beams = defaultdict(int)
    beams[data[0].index("S")] = 1
    splitted = 0
    for line in data[1:]:
        new_beams = beams.copy()
        for b in beams:
            if beams[b] > 0 and line[b] == "^":
                new_beams[b] -= beams[b]
                splitted += 1
                if b > 1:
                    new_beams[b - 1] += beams[b]
                if b < len(line) - 1:
                    new_beams[b + 1] += beams[b]
        beams = new_beams

    return sum(beams.values()) + 1


if __name__ == "__main__":
    from utils import download_puzzle_input, run

    download_puzzle_input()
    run(part_1, "data/day07-example.txt", expected=21)
    run(part_1, "data/day07-data.txt")
    run(part_2, "data/day07-example.txt", expected=40)
    run(part_2, "data/day07-data.txt")
