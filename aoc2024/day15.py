# Advent of Code 2024, Day 15
# https://adventofcode.com/2024/day/15


# Part One
def load_map(file_name):
    data = open(file_name, "r").read()
    grid, moves = data.split("\n\n")
    grid = grid.strip().split("\n")
    grid = [list(line) for line in grid]
    moves = moves.strip().replace("\n", "")
    robot = next(
        (x, y) for y, line in enumerate(grid) for x, c in enumerate(line) if c == "@"
    )
    d = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}
    moves = list(map(d.get, moves))
    return grid, robot, moves


def move(grid, pos, direction):
    x = pos[0] + direction[0]
    y = pos[1] + direction[1]

    if grid[y][x] == "#":
        return False

    if grid[y][x] == "O":
        if not move(grid, (x, y), direction):
            return False

    grid[y][x] = grid[pos[1]][pos[0]]
    grid[pos[1]][pos[0]] = "."
    return True


def part_1(file_name):
    grid, robot, moves = load_map(file_name)
    for m in moves:
        if move(grid, robot, m):
            robot = (robot[0] + m[0], robot[1] + m[1])
    boxes = (
        x + y * 100
        for y, line in enumerate(grid)
        for x, c in enumerate(line)
        if c == "O"
    )
    return sum(boxes)


def expand_grid(grid):
    exp = {".": "..", "#": "##", "O": "[]", "@": "@."}
    return [[y for x in row for y in exp[x]] for row in grid]


def move2(grid, pos, direction, do_move):
    x = pos[0] + direction[0]
    y = pos[1] + direction[1]
    if grid[y][x] == "#":
        return False
    if grid[y][x] == "[" or grid[y][x] == "]":
        if direction[1] != 0:
            if grid[y][x] == "[" and not move2(grid, (x + 1, y), direction, do_move):
                return False
            if grid[y][x] == "]" and not move2(grid, (x - 1, y), direction, do_move):
                return False
        if not move2(grid, (x, y), direction, do_move):
            return False
    if do_move:
        grid[y][x] = grid[pos[1]][pos[0]]
        grid[pos[1]][pos[0]] = "."
    return True


def part_2(file_name):
    grid, robot, moves = load_map(file_name)
    grid = expand_grid(grid)
    robot = (2 * robot[0], robot[1])
    for m in moves:
        if move2(grid, robot, m, False):
            move2(grid, robot, m, True)
            robot = (robot[0] + m[0], robot[1] + m[1])
    boxes = (
        x + y * 100
        for y, line in enumerate(grid)
        for x, c in enumerate(line)
        if c == "["
    )
    return sum(boxes)


if __name__ == "__main__":
    from utils import run

    run(part_1, "data/day15-example1.txt", expected=2028)
    run(part_1, "data/day15-example2.txt", expected=10092)
    run(part_1, "data/day15-data.txt", expected=1511865)
    run(part_2, "data/day15-example2.txt", expected=9021)
    run(part_2, "data/day15-data.txt", expected=1519991)
