# Advent of Code 2024, Day 0
# https://adventofcode.com/2024/day/


# Part One
def load_data(file_name):
    data = open(file_name, "r").readlines()
    return (map(int, line.split()) for line in data)


def fn_1(data):
    return []


def part_1(file_name):
    return sum(fn_1(load_data(file_name)))


# Part Two
def fn_2(data):
    return []


def part_2(file_name):
    return sum(fn_2(load_data(file_name)))


if __name__ == "__main__":
    print("1. Example:", part_1("data/day00-example.txt"), "=? #")
    # print("1. Answer:", part_1("data/day00-data.txt"))
    # print("2. Example:", part_2("data/day00-example.txt"), "=? #")
    # print("2. Answer:", part_2("data/day00-data.txt"))
