# Advent of Code 2025, Day 4
# https://adventofcode.com/2025/day/4

from grid import convolve, center, count_if, count


def load_data(input_file: str):
    return [list(line) for line in open(input_file).read().strip().split("\n")]


# Part One
def can_move(grid, roi):
    ctr = center(grid, roi)
    is_roll = ctr == "@"
    return is_roll and count_if(grid, "@", roi) <= 4


def part_1(input_file):
    grid = load_data(input_file)

    moved_map = convolve(grid, fn=can_move)
    n_moved = count(moved_map)
    return n_moved


# Part Two
def move(grid, roi):
    ctr = center(grid, roi)
    is_roll = ctr == "@"
    can_be_moved = is_roll and count_if(grid, "@", roi) <= 4
    return can_be_moved, ("." if can_be_moved else ctr)


def part_2(input_file):
    grid = load_data(input_file)

    total = 0
    while True:
        moved_map = convolve(grid, fn=move, update=True)
        n_moved = count(moved_map)
        if n_moved == 0:
            break
        total += n_moved
    return total


if __name__ == "__main__":
    from utils import run, download_puzzle_input

    download_puzzle_input()
    run(part_1, "data/day04-example.txt", expected=13)
    run(part_1, "data/day04-data.txt", expected=1437)
    run(part_2, "data/day04-example.txt", expected=43)
    run(part_2, "data/day04-data.txt", expected=8765)
