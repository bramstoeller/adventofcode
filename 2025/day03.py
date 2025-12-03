# Advent of Code 2025, Day 3
# https://adventofcode.com/2025/day/3

def load_data(input_file: str):
    return open(input_file).read().strip().split('\n')


# Part One

def argmax(array):
    return max(array), array.index(max(array))


def part_1(input_file):
    data = load_data(input_file)
    total = 0
    for battery in data:
        a, i = argmax(battery[:-1])
        b = max(battery[i + 1:])
        c = 10 * int(a) + int(b)
        total += c
    return total


# Part Two

def part_2(input_file, n: int):
    data = load_data(input_file)
    total = 0
    for battery in data:
        val = 0
        idx0 = 0
        for i in range(n):
            idx1 = len(battery) - n + i + 1
            v, idx = argmax(battery[idx0:idx1])
            idx0 = idx0 + idx + 1
            val += int(v) * (10 ** (n - i - 1))
        total += val
    return total


if __name__ == "__main__":
    from utils import run

    run(part_1, "data/day03-example.txt", expected=357)
    x = run(part_1, "data/day03-data.txt")
    run(part_2, "data/day03-data.txt", n=2, expected=x)
    run(part_2, "data/day03-example.txt", n=12, expected=3121910778619)
    run(part_2, "data/day03-data.txt", n=12)
