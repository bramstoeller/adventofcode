# Advent of Code 2025, Day 11
# https://adventofcode.com/2025/day/11


def load_data(input_file: str):
    lines = open(input_file).read().strip().split("\n")
    return {device: output.split() for device, output in (line.split(": ") for line in lines)}


def find_all_paths(edges, current, goal):
    def depth_first_search(current):
        return current == goal or sum(depth_first_search(neighbor) for neighbor in edges[current])

    return depth_first_search(current)


# Part One
def part_1(input_file):
    return find_all_paths(load_data(input_file), "you", "out")


# Part Two


def count_all_paths(edges, start, goal, required_keys):
    cache = dict()

    def depth_first_count(current, keys):
        if current == goal:
            return keys == required_keys
        cache_key = current, tuple(sorted(keys))
        if cache_key not in cache:
            cache[cache_key] = sum(depth_first_count(nb, keys | (required_keys & {nb})) for nb in edges[current])
        return cache[cache_key]

    return depth_first_count(start, set())


def part_2(input_file):
    return count_all_paths(load_data(input_file), "svr", "out", {"dac", "fft"})


if __name__ == "__main__":
    from utils import download_puzzle_input, run

    download_puzzle_input()
    run(part_1, "data/day11-example.txt", expected=5)
    run(part_1, "data/day11-data.txt")
    run(part_2, "data/day11-example2.txt", expected=2)
    run(part_2, "data/day11-data.txt")
