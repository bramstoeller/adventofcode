# Advent of Code 2024, Day 11
# https://adventofcode.com/2024/day/11

# Part One
from itertools import chain


def load_data(file_name):
    return map(int, open(file_name, "r").read().strip().split())


def blink(stone):
    if stone == 0:
        yield 1
        return
    s = str(stone)
    n = len(s)
    if n % 2 == 0:
        yield int(s[:n // 2])
        yield int(s[n // 2:])
    else:
        yield stone * 2024


def gen_stone_list(stones, depth):
    for _ in range(depth):
        stones = chain(*(blink(stone) for stone in stones))
    return list(stones)


def part_1(file_name, depth):
    return len(gen_stone_list(load_data(file_name), depth))


# Part Two
cache = {}


def calc_num_stones(stone, depth):
    if depth == 0:
        return 1
    if (depth, stone) not in cache:
        cache[(depth, stone)] = sum(calc_num_stones(s, depth - 1) for s in blink(stone))
    return cache[(depth, stone)]


def part_2(file_name, depth):
    return sum(calc_num_stones(stone, depth) for stone in load_data(file_name))


if __name__ == "__main__":
    print("1. Example:", part_1("data/day11-example.txt", 25), "=? 55312")
    print("1. Answer:", part_1("data/day11-data.txt", 25))
    print("2. Example:", part_2("data/day11-example.txt", 25), "=? 55312")
    print("2. Answer:", part_2("data/day11-data.txt", 75))
    print("Cached nodes: ", len(cache))
