# Advent of Code 2024, Day 16
# https://adventofcode.com/2024/day/16


# Part One
def load_map(file_name):
    grid = [line.strip() for line in open(file_name, "r").readlines()]
    start = next(
        (x, y, 1, 0)
        for y, row in enumerate(grid)
        for x, c in enumerate(row)
        if c == "S"
    )
    end = next(
        (x, y) for y, row in enumerate(grid) for x, c in enumerate(row) if c == "E"
    )
    return grid, start, end


def fn_1(grid, start, end):
    open_set = {start}
    closed_set = {start: 0}
    while open_set:
        x, y, dx, dy = open_set.pop()
        for ndx, ndy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            cost = (
                1
                if (dx, dy) == (ndx, ndy)
                else 1001
                if dx != ndx or dy != ndy
                else 2001
            )
            nx, ny = x + ndx, y + ndy
            if grid[ny][nx] == "#":
                continue
            if (nx, ny, ndx, ndy) in closed_set and closed_set[
                (nx, ny, ndx, ndy)
            ] <= closed_set[(x, y, dx, dy)] + cost:
                continue
            open_set.add((nx, ny, ndx, ndy))
            closed_set[(nx, ny, ndx, ndy)] = closed_set[(x, y, dx, dy)] + cost

    return [
        closed_set[end[0], end[1], dx, dy]
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]
        if (end[0], end[1], dx, dy) in closed_set
    ]


def part_1(file_name):
    return min(fn_1(*load_map(file_name)))


# Part Two
def fn_2(grid: list[str], start: tuple[int, int, int, int], end: tuple[int, int]):
    open_set = {start}
    closed_set: dict[
        tuple[int, int, int, int], tuple[int, list[tuple[int, int, int, int]]]
    ] = {start: (0, [])}
    while open_set:
        x, y, dx, dy = open_set.pop()
        for ndx, ndy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            cost = (
                1
                if (dx, dy) == (ndx, ndy)
                else 1001
                if dx != ndx or dy != ndy
                else 2001
            )
            nx, ny = x + ndx, y + ndy
            if grid[ny][nx] == "#":
                continue
            if (nx, ny, ndx, ndy) in closed_set:
                if (
                    closed_set[(nx, ny, ndx, ndy)][0]
                    < closed_set[(x, y, dx, dy)][0] + cost
                ):
                    continue
                if (
                    closed_set[(nx, ny, ndx, ndy)][0]
                    == closed_set[(x, y, dx, dy)][0] + cost
                ):
                    closed_set[(nx, ny, ndx, ndy)][1].append((x, y, dx, dy))
                else:
                    closed_set[(nx, ny, ndx, ndy)] = (
                        closed_set[(x, y, dx, dy)][0] + cost,
                        [(x, y, dx, dy)],
                    )
            else:
                closed_set[(nx, ny, ndx, ndy)] = (
                    closed_set[(x, y, dx, dy)][0] + cost,
                    [(x, y, dx, dy)],
                )
            open_set.add((nx, ny, ndx, ndy))

    x, y = end
    end_points = {
        (x, y, dx, dy): closed_set[x, y, dx, dy]
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]
        if (x, y, dx, dy) in closed_set
    }
    open_set = {k for k, v in end_points.items() if v == min(end_points.values())}
    visited = set()
    while open_set:
        x, y, dx, dy = open_set.pop()
        visited.add((x, y, dx, dy))
        _, origin = closed_set[(x, y, dx, dy)]
        open_set |= set(origin) - visited

    return {(x, y) for x, y, _, _ in visited}


def part_2(file_name):
    return len(fn_2(*load_map(file_name)))


if __name__ == "__main__":
    from utils import run

    run(part_1, "data/day16-example1.txt", expected=7036)
    run(part_1, "data/day16-example2.txt", expected=11048)
    run(part_1, "data/day16-data.txt", expected=101492)
    run(part_2, "data/day16-example1.txt", expected=45)
    run(part_2, "data/day16-example2.txt", expected=64)
    run(part_2, "data/day16-data.txt", expected=543)
