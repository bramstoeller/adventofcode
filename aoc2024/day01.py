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
    print("1. Example:", part_1("data/day01-example.txt"), "=? 11")
    print("1. Answer:", part_1("data/day01-data.txt"))
    print("2. Example:", part_2("data/day01-example.txt"), "=? 31")
    print("2. Answer:", part_2("data/day01-data.txt"))
