# Advent of Code 2025, Day 4
# https://adventofcode.com/2025/day/4


def load_data(input_file: str):
    return [list(line) for line in open(input_file).read().strip().split("\n")]


# Part One
def count_nbh(grid, x, y):
    h, w = len(grid), len(grid[0])
    xr = range(max(0, x - 1), min(w, x + 2))
    yr = range(max(0, y - 1), min(h, y + 2))
    return sum(grid[j][i] == "@" for j in yr for i in xr)


def part_1(input_file):
    grid = load_data(input_file)
    h, w = len(grid), len(grid[0])
    xr, yr = range(w), range(h)
    movable = (grid[y][x] == "@" and count_nbh(grid, x, y) <= 4 for y in yr for x in xr)
    return sum(movable)


# Part Two
def part_2(input_file):
    grid = load_data(input_file)
    h, w = len(grid), len(grid[0])
    total = 0
    moving = True
    while moving:
        moving = False
        for y in range(h):
            for x in range(w):
                if grid[y][x] == "@" and count_nbh(grid, x, y) <= 4:
                    moving = True
                    grid[y][x] = " "
                    total += 1
    return total


if __name__ == "__main__":
    from utils import run, download_puzzle_input

    download_puzzle_input()
    run(part_1, "data/day04-example.txt", expected=13)
    run(part_1, "data/day04-data.txt", expected=1437)
    run(part_2, "data/day04-example.txt", expected=43)
    run(part_2, "data/day04-data.txt", expected=8765)
