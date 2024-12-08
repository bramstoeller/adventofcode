# Advent of Code 2024, Day 7
# https://adventofcode.com/2024/day/7


# Part One
def read_equations(file_name):
    for line in open(file_name, "r"):
        answer, values = line.split(":")
        yield int(answer), map(int, values.split())


def calc(values, operators):
    answers = []
    a, b, *y = values
    for fn in operators:
        x = fn(a, b)
        answers += calc([x] + y, operators) if y else [x]
    return answers


def part_1(file_name):
    operators = [lambda x, y: x + y, lambda x, y: x * y]
    return sum(answer for answer, values in read_equations(file_name) if answer in calc(values, operators))


# Part Two
def part_2(file_name):
    concat = lambda x, y: int(str(x) + str(y))
    operators = [lambda x, y: x + y, lambda x, y: x * y, concat]
    return sum(answer for answer, values in read_equations(file_name) if answer in calc(values, operators))


if __name__ == "__main__":
    print("1. Example:", part_1("data/day07-example.txt"), "=? 3749")
    print("1. Answer:", part_1("data/day07-data.txt"))
    print("2. Example:", part_2("data/day07-example.txt"), "=? 11387")
    print("2. Answer:", part_2("data/day07-data.txt"))
