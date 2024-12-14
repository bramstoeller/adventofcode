# Advent of Code 2024, Day 14
# https://adventofcode.com/2024/day/14


# Part One
import re

PATTERN = re.compile(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)")


def load_data(file_name):
    return [re.match(PATTERN, line).groups() for line in open(file_name, "r")]


def move(robots, size, moves):
    grid = [[0] * size[0] for _ in range(size[1])]
    w, h = size
    for x, y, vx, vy in robots:
        x = (int(x) + int(vx) * moves) % w
        y = (int(y) + int(vy) * moves) % h
        grid[int(y)][int(x)] += 1
    return grid


def part_1(file_name, size, moves):
    grid = move(load_data(file_name), size, moves)
    w, h = size
    q1 = sum(sum(n for n in row[:w // 2]) for row in grid[:h // 2])
    q2 = sum(sum(n for n in row[w // 2 + 1:]) for row in grid[:h // 2])
    q3 = sum(sum(n for n in row[:w // 2]) for row in grid[h // 2 + 1:])
    q4 = sum(sum(n for n in row[w // 2 + 1:]) for row in grid[h // 2 + 1:])
    return q1 * q2 * q3 * q4


# Part Two
import os
import time


def find_christmas_tree(robots, size, moves):
    grid = move(robots, size, moves)
    w, h = size
    if not any(sum(n for n in row) > w / 4 for row in grid):
        return
    os.system('clear')
    for row in grid[::2]:
        print(''.join('#' if n else ' ' for n in row))
    print("MOVES:", moves)
    time.sleep(0.4)


def part_2(file_name, size, max_moves):
    robots = load_data(file_name)
    for i in range(max_moves):
        try:
            find_christmas_tree(robots, size, i)
        except KeyboardInterrupt:
            return i
    return None


if __name__ == "__main__":
    print("1. Example:", part_1("data/day14-example.txt", (11, 7), 100), "=? 12")
    print("1. Answer:", part_1("data/day14-data.txt", (101, 103), 100))
    part_2("data/day14-data.txt", (101, 103), 10000)
