# Advent of Code 2025, Day 4
# https://adventofcode.com/2025/day/4


def load_data(input_file: str):
    return [list(line) for line in open(input_file).read().strip().split("\n")]


# Part One
def count_nbh(grid, x, y):
    count = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
                count += grid[ny][nx] == "@"
    return count


def part_1(input_file):
    grid = load_data(input_file)
    count_grid = [[0] * len(grid[0]) for _ in range(len(grid))]
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            count_grid[y][x] = grid[y][x] != "." and count_nbh(grid, x, y) < 4
    return sum(sum(row) for row in count_grid)


# Part Two
def part_2(input_file):
    grid = load_data(input_file)
    count_grid = [[0] * len(grid[0]) for _ in range(len(grid))]
    total = 0
    while True:
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                count_grid[y][x] = grid[y][x] != "." and count_nbh(grid, x, y) < 4
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if count_grid[y][x]:
                    grid[y][x] = "."
        x = sum(sum(row) for row in count_grid)
        if x == 0:
            break
        total += x
    return total


if __name__ == "__main__":
    from utils import run

    run(part_1, "data/day04-example.txt", expected=13)
    run(part_1, "data/day04-data.txt")
    run(part_2, "data/day04-example.txt", expected=43)
    run(part_2, "data/day04-data.txt")
