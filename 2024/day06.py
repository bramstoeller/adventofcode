# Advent of Code 2024, Day 6
# https://adventofcode.com/2024/day/6


# Part One
def read_map(file_name):
    directions = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}
    data = open(file_name, "r").read().strip().splitlines()
    obstacles = set((x, y) for y, line in enumerate(data) for x, c in enumerate(line) if c == "#")
    pos, dir_char = next(((x, y), c) for y, line in enumerate(data) for x, c in enumerate(line) if c in directions)
    direction = directions[dir_char]
    max_x = len(data[0]) - 1
    max_y = len(data) - 1
    return obstacles, pos, direction, max_x, max_y


def turn_right(direction):
    return {(0, -1): (1, 0), (0, 1): (-1, 0), (-1, 0): (0, -1), (1, 0): (0, 1)}[direction]


def move_forward(pos, direction):
    return pos[0] + direction[0], pos[1] + direction[1]


def move(obstacles, pos, direction, max_x, max_y):
    visited = set()
    while pos[0] >= 0 and pos[0] <= max_x and pos[1] >= 0 and pos[1] <= max_y:
        visited.add(pos)
        while move_forward(pos, direction) in obstacles:
            direction = turn_right(direction)
        pos = move_forward(pos, direction)
    return visited


def part_1(files_name):
    return len(move(*read_map(files_name)))


# Part Two
def has_loop(obstacles, pos, direction, max_x, max_y):
    visited = set()
    while pos[0] >= 0 and pos[0] <= max_x and pos[1] >= 0 and pos[1] <= max_y:
        if (pos, direction) in visited:
            return True
        visited.add((pos, direction))
        while move_forward(pos, direction) in obstacles:
            direction = turn_right(direction)
        pos = move_forward(pos, direction)
    return False


def find_obstruction_positions(obstacles, pos, direction, max_x, max_y):
    candidates = move(obstacles, pos, direction, max_x, max_y)

    obstructions = set()
    for obs in candidates:
        if has_loop(obstacles | {obs}, pos, direction, max_x, max_y):
            obstructions.add(obs)
    return obstructions


def part_2(file_name):
    return len(find_obstruction_positions(*read_map(file_name)))


if __name__ == "__main__":
    print("1. Example:", part_1("data/day06-example.txt"), "=? 41")
    print("1. Answer:", part_1("data/day06-data.txt"))
    print("2. Example:", part_2("data/day06-example.txt"), "=? 6")
    print("2. Answer:", part_2("data/day06-data.txt"))
