# Advent of Code 2025, Day 2
# https://adventofcode.com/2025/day/2
from itertools import chain
from typing import Iterator


def load_data(input_file: str) -> Iterator[int]:
    pairs = open(input_file).read().strip().split(",")
    boundaries = (p.split("-") for p in pairs)
    ranges = (range(int(a), int(b) + 1) for a, b in boundaries)
    return chain.from_iterable(ranges)


# Part One
def is_invalid_1(id):
    sid = str(id)
    n = len(sid)
    return not n % 2 and sid[: n // 2] == sid[n // 2 :]


def part_1(input_file):
    ids = load_data(input_file)
    invalid_ids = [i for i in ids if is_invalid_1(i)]
    return sum(int(i) for i in invalid_ids)


# Part Two
def is_invalid_2(id):
    sid = str(id)
    id_len = len(sid)
    for part_len in range(1, id_len // 2 + 1):
        if id_len % part_len:
            continue
        n_parts = id_len // part_len
        if all(sid[:part_len] == sid[i * part_len : (i + 1) * part_len] for i in range(1, n_parts)):
            return True
    return False


def part_2(input_file):
    ids = load_data(input_file)
    invalid_ids = (i for i in ids if is_invalid_2(i))
    return sum(int(i) for i in invalid_ids)


if __name__ == "__main__":
    from utils import run

    run(part_1, "data/day02-example.txt", expected=1227775554)
    run(part_1, "data/day02-data.txt", expected=23701357374)
    run(part_2, "data/day02-example.txt", expected=4174379265)
    run(part_2, "data/day02-data.txt", expected=34284458938)
