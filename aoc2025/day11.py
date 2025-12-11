# Advent of Code 2025, Day 11
# https://adventofcode.com/2025/day/11
from functools import cache


def load_data(input_file: str):
    lines = open(input_file).read().strip().split("\n")
    return {device: output.split() for device, output in (line.split(": ") for line in lines)}


# Part One
def count_all_paths_1(edges, start, goal):
    @cache
    def depth_first_search(current):
        return current == goal or sum(depth_first_search(neighbor) for neighbor in edges[current])

    return depth_first_search(start)


def part_1(input_file):
    return count_all_paths_1(load_data(input_file), "you", "out")


# Part Two
def count_all_paths_2(edges, start, goal, required_keys):
    @cache
    def depth_first_search(current: str, *keys: bool):
        if current == goal:
            return all(keys)
        nbh = ((nb, tuple(k or (nb == rk) for k, rk in zip(keys, required_keys))) for nb in edges[current])
        return sum(depth_first_search(nb, *keys) for nb, keys in nbh)

    return depth_first_search(start, *(False for _ in required_keys))


def part_2(input_file):
    return count_all_paths_2(load_data(input_file), "svr", "out", ("dac", "fft"))


if __name__ == "__main__":
    from utils import download_puzzle_input, run

    download_puzzle_input()
    run(part_1, "data/day11-example.txt", expected=5)
    run(part_1, "data/day11-data.txt", expected=511)
    run(part_2, "data/day11-example2.txt", expected=2)
    run(part_2, "data/day11-data.txt", expected=458618114529380)
