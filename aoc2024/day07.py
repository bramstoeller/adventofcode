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
    def concat(x, y):
        return int(str(x) + str(y))

    operators = [lambda x, y: x + y, lambda x, y: x * y, concat]
    return sum(answer for answer, values in read_equations(file_name) if answer in calc(values, operators))


if __name__ == "__main__":
    from utils import run

    run(part_1, "data/day07-example.txt", expected=3749)
    run(part_1, "data/day07-data.txt", expected=1298300076754)
    run(part_2, "data/day07-example.txt", expected=11387)
    run(part_2, "data/day07-data.txt", expected=248427118972289)
