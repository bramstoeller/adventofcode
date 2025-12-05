# Advent of Code 2025, Day 5
# https://adventofcode.com/2025/day/5


def load_data(input_file: str):
    data = open(input_file).read().strip()
    range_s, ids_s = data.split("\n\n")
    range_t = (r.split("-") for r in range_s.split("\n"))
    ranges = (range(int(r[0]), int(r[1]) + 1) for r in range_t)
    ids = (int(i) for i in ids_s.split("\n"))
    return list(ranges), list(ids)


# Part One
def part_1(input_file):
    ranges, ids = load_data(input_file)
    return sum(1 for i in ids if any(i in r for r in ranges))


# Part Two
def merge_ranges(ranges):
    ranges = sorted(ranges, key=lambda r: r.start)
    merged = []
    for r in ranges:
        if not merged or merged[-1].stop < r.start:
            merged.append(r)
        else:
            merged[-1] = range(merged[-1].start, max(merged[-1].stop, r.stop))
    return merged


def part_2(input_file):
    ranges, _ = load_data(input_file)
    merged = merge_ranges(ranges)
    return sum(r.stop - r.start for r in merged)


if __name__ == "__main__":
    from utils import download_puzzle_input, run

    download_puzzle_input()
    run(part_1, "data/day05-example.txt", expected=3)
    run(part_1, "data/day05-data.txt", expected=509)
    run(part_2, "data/day05-example.txt", expected=14)
    run(part_2, "data/day05-data.txt", expected=336790092076620)
