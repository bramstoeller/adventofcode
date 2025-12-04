# Advent of Code 2024, Day 1
# https://adventofcode.com/2024/day/1


# Part One
def load_data(file_name):
    data = open(file_name, "r").readlines()
    return zip(*(map(int, line.split()) for line in data))


def distance(A, B):
    return (abs(a - b) for a, b in zip(sorted(A), sorted(B)))


def part_1(file_name):
    return sum(distance(*load_data(file_name)))


# Part Two
def similarity(A, B):
    return (a * sum(b == a for b in B) for a in A)


def part_2(file_name):
    return sum(similarity(*load_data(file_name)))


if __name__ == "__main__":
    from utils import run

    run(part_1, "data/day01-example.txt", expected=11)
    run(part_1, "data/day01-data.txt", expected=1830467)
    run(part_2, "data/day01-example.txt", expected=31)
    run(part_2, "data/day01-data.txt", expected=26674158)
