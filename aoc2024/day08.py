# Advent of Code 2024, Day 8
# https://adventofcode.com/2024/day/8

from collections import defaultdict
from itertools import chain, combinations

# Part One


def read_map(file_name):
    data = [line.strip() for line in open(file_name)]
    antennas = defaultdict(list)
    for x, y, c in ((x, y, c) for y, line in enumerate(data) for x, c in enumerate(line) if c != "."):
        antennas[c].append(x + y * 1j)
    return dict(antennas), (len(data[0]) - 1) + (len(data) - 1) * 1j


def on_map(p, p_max):
    return 0 <= p.real <= p_max.real and 0 <= p.imag <= p_max.imag


def find_anti_antennas(antennas, p_max):
    anti_antennas = {p - (q - p) for antenna, points in antennas.items() for p, q in combinations(points, 2)}
    anti_antennas |= {q + (q - p) for antenna, points in antennas.items() for p, q in combinations(points, 2)}
    return {p for p in anti_antennas if on_map(p, p_max)}


def part_1(file_name):
    return len(find_anti_antennas(*read_map(file_name)))


# Part Two


def pt_range(p, q, p_max):
    d = q - p
    n1 = min(
        p.real // d.real if d.real > 0 else (p_max.real - p.real) // -d.real,
        p.imag // d.imag if d.imag > 0 else (p_max.imag - p.imag) // -d.imag,
    )
    n2 = min(
        (p_max.real - p.real) // d.real if d.real > 0 else p.real // -d.real,
        (p_max.imag - p.imag) // d.imag if d.imag > 0 else p.imag // -d.imag,
    )
    return {p + n * d for n in range(-int(n1), int(n2 + 1))}


def find_all_anti_antennas(antennas, max_p):
    anti_antennas = (pt_range(p, q, max_p) for _, points in antennas.items() for p, q in combinations(points, 2))
    return set(chain(*anti_antennas))


def part_2(file_name):
    return len(find_all_anti_antennas(*read_map(file_name)))


if __name__ == "__main__":
    from utils import run

    run(part_1, "data/day08-example.txt", expected=14)
    run(part_1, "data/day08-data.txt", expected=367)
    run(part_2, "data/day08-example.txt", expected=34)
    run(part_2, "data/day08-data.txt", expected=1285)
