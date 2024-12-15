# Advent of Code 2024, Day 15
# https://adventofcode.com/2024/day/15


# Part One
def load_map(file_name):
    data = open(file_name, "r").read()
    grid, moves = data.split("\n\n")
    grid = grid.strip().split("\n")
    moves = moves.strip().replace("\n", "")
    walls = {x + y * 1j for y, line in enumerate(grid) for x, c in enumerate(line) if c == '#'}
    boxes = {x + y * 1j for y, line in enumerate(grid) for x, c in enumerate(line) if c == 'O'}
    robot = next(x + y * 1j for y, line in enumerate(grid) for x, c in enumerate(line) if c == '@')
    d = {'^': -1j, '>': 1, 'v': 1j, '<': -1}
    moves = list(map(d.get, moves))
    return walls, boxes, robot, moves


def move(walls, boxes, pos, direction):
    pos += direction
    if pos in walls:
        return False
    if pos in boxes:
        if not move(walls, boxes, pos, direction):
            return False
        boxes.remove(pos)
        boxes.add(pos + direction)
    return True


def part_1(file_name):
    walls, boxes, robot, moves = load_map(file_name)
    for m in moves:
        if move(walls, boxes, robot, m):
            robot += m
    return sum(int(b.real + b.imag * 100) for b in boxes)


# Part Two
def fn_2(data):
    return []


def part_2(file_name):
    return sum(fn_2(load_map(file_name)))


if __name__ == "__main__":
    print("1. Example1:", part_1("data/day15-example1.txt"), "=? 2028")
    print("1. Example2:", part_1("data/day15-example2.txt"), "=? 10092")
    print("1. Answer:", part_1("data/day15-data.txt"))
    # print("2. Example:", part_2("data/day00-example.txt"), "=? #")  # print("2. Answer:", part_2("data/day00-data.txt"))
