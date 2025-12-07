# Advent of Code 2024, Day 3
# https://adventofcode.com/2024/day/3
import re


# Part One
def load_data(file_name):
    return open(file_name, "r").read()


def find_mul_instructions(data, pattern):
    for match in pattern.finditer(data):
        yield (int(x) for x in match.groups())


def part_1(file_name):
    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    data = load_data(file_name)
    return sum(a * b for a, b in find_mul_instructions(data, pattern))


# Part Two
def find_do_dont_instructions(data, pattern):
    enabled = True
    for match in pattern.finditer(data):
        txt, a, b = match.groups()
        if txt == "do()":
            enabled = True
        elif txt == "don't()":
            enabled = False
        elif enabled:
            yield int(a), int(b)


def part_2(file_name):
    pattern = re.compile(r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\))")
    data = load_data(file_name)
    return sum(a * b for a, b in find_do_dont_instructions(data, pattern))


if __name__ == "__main__":
    from utils import run

    run(part_1, "data/day03-example1.txt", expected=161)
    run(part_1, "data/day03-data.txt", expected=160672468)
    run(part_2, "data/day03-example2.txt", expected=48)
    run(part_2, "data/day03-data.txt", expected=84893551)
