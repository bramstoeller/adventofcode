# Advent of Code 2024, Day 02
# https://adventofcode.com/2024/day/2


# Part One
def load_data(file_name):
    for line in open(file_name, "r"):
        yield list(map(int, line.split()))


def is_save_1(report):
    values_pairs = zip(report[:-1], report[1:])
    if report[0] < report[1]:  # increasing
        return all(1 <= b - a <= 3 for a, b in values_pairs)
    if report[0] > report[1]:  # decreasing
        return all(1 <= a - b <= 3 for a, b in values_pairs)
    return False  # stable


def part_1(file_name):
    return sum(is_save_1(report) for report in load_data(file_name))


# Part Two
def is_save_2(report):
    return any(is_save_1(report[:i] + report[i + 1:]) for i in range(len(report)))


def part_2(file_name):
    return sum(is_save_2(report) for report in load_data(file_name))


if __name__ == "__main__":
    print("1. Example:", part_1("data/day02-example.txt"), "=? 2")
    print("1. Answer:", part_1("data/day02-data.txt"))
    print("2. Example:", part_2("data/day02-example.txt"), "=? 4")
    print("2. Answer:", part_2("data/day02-data.txt"))
