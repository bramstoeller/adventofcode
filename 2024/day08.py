# Advent of Code 2024, Day 8
# https://adventofcode.com/2024/day/8
from itertools import combinations


# Part One
def read_map(file_name):
    data = open(file_name, "r").read().strip().splitlines()
    antennas = {(x, y): c for y, line in enumerate(data) for x, c in enumerate(line) if c != "."}
    antennas = {antenna: [p for p, a in antennas.items() if a == antenna] for antenna in set(antennas.values())}
    max_x = len(data[0]) - 1
    max_y = len(data) - 1
    return antennas, max_x, max_y


def find_anti_antennas(antennas):
    anti_antennas = set()
    for antenna, points in antennas.items():
        for p, q in combinations(points, 2):
            if p == q:
                continue
            dx = p[0] - q[0]
            dy = p[1] - q[1]
            anti_antennas.add((p[0] + dx, p[1] + dy))
            anti_antennas.add((q[0] - dx, q[1] - dy))
    return anti_antennas


def part_1(file_name):
    antennas, max_x, max_y = read_map(file_name)
    return len(set((x, y) for x, y in find_anti_antennas(antennas) if 0 <= x <= max_x and 0 <= y <= max_y))


# Part Two
def fn_2(data):
    return []


def part_2(file_name):
    return sum(fn_2(load_data(file_name)))


if __name__ == "__main__":
    print("1. Example:", part_1("data/day08-example.txt"), "=? 14")
    print("1. Answer:", part_1("data/day08-data.txt"))
    # print("2. Example:", part_2("data/day00-example.txt"), "=? #")
    # print("2. Answer:", part_2("data/day00-data.txt"))
