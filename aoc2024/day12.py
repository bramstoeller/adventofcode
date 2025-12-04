# Advent of Code 2024, Day 12
# https://adventofcode.com/2024/day/12


# Part One
def read_map(file_name):
    data = open(file_name, "r").readlines()
    return {x + y * 1j: c for y, line in enumerate(data) for x, c in enumerate(line.strip())}


def find_4cc(p, grid):
    open_set = {p}
    plant = grid[p]
    garden = []
    while open_set:
        p = open_set.pop()
        grid[p] = "."
        garden.append(p)
        for d in (1j**i for i in range(4)):
            n = p + d
            if grid.get(n) == plant:
                open_set.add(n)
    return garden


def calculate_perimeter(garden):
    perimeter = 0
    for p in garden:
        for d in (1j**i for i in range(4)):
            n = p + d
            if n not in garden:
                perimeter += 1
    return perimeter


def find_gardens(grid):
    for p, c in grid.items():
        if c == ".":
            continue
        garden = find_4cc(p, grid)
        if garden:
            yield garden


def part_1(file_name):
    gardens = find_gardens(read_map(file_name))
    return sum(len(g) * calculate_perimeter(g) for g in gardens)


def count_contiguous_fences(fences, directions):
    cnt = 0
    while fences:
        cnt += 1
        open_set = {fences.pop()}
        while open_set:
            p, q = open_set.pop()
            for d in directions:
                n = (p + d, q + d)
                if n in fences:
                    open_set.add(n)
                    fences.remove(n)
    return cnt


def get_perimeter_sides(garden, directions):
    return {(p, p + d) for p in garden for d in directions if p + d not in garden}


def count_perimeter_sides(garden):
    v = get_perimeter_sides(garden, [-1j, 1j])
    h = get_perimeter_sides(garden, [-1, 1])
    return count_contiguous_fences(v, [-1, 1]) + count_contiguous_fences(h, [-1j, 1j])


def part_2(file_name):
    gardens = find_gardens(read_map(file_name))
    return sum(len(g) * count_perimeter_sides(g) for g in gardens)


if __name__ == "__main__":
    from utils import run

    run(part_1, "data/day12-example1-1.txt", expected=140)
    run(part_1, "data/day12-example1-2.txt", expected=772)
    run(part_1, "data/day12-example1-3.txt", expected=1930)
    run(part_1, "data/day12-data.txt", expected=1464678)
    run(part_2, "data/day12-example1-1.txt", expected=80)
    run(part_2, "data/day12-example1-2.txt", expected=436)
    run(part_2, "data/day12-example2-1.txt", expected=236)
    run(part_2, "data/day12-example2-2.txt", expected=368)
    run(part_2, "data/day12-example1-3.txt", expected=1206)
    run(part_2, "data/day12-data.txt", expected=877492)
