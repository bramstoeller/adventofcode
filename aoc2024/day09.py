# Advent of Code 2024, Day 9
# https://adventofcode.com/2024/day/9


# Part One
from itertools import chain


def read_disk(file_name):
    return (int(n) for n in open(file_name, "r").read().strip())


def decompress_1(disk):
    return list(
        chain(*([i // 2 if i % 2 == 0 else None] * n for i, n in enumerate(disk)))
    )


def defrag_1(disk):
    n = len(disk)
    front = 0
    back = n - 1
    while front < back:
        if disk[front] is None:
            while disk[back] is None:
                back -= 1
            if front > back:
                break
            disk[front] = disk[back]
            disk[back] = None
            back -= 1
        front += 1
    return disk


def checksum(disk):
    return sum(i * id if id is not None else 0 for i, id in enumerate(disk))


def part_1(file_name):
    return checksum(defrag_1(decompress_1(read_disk(file_name))))


# Part Two


def decompress_2(disk):
    return list((i // 2 if i % 2 == 0 else None, n) for i, n in enumerate(disk))


def defrag_2(disk):
    back = len(disk)
    while back > 0:
        back -= 1
        id, n = disk[back]
        if id is None:
            continue
        for front in range(back):
            front_id, space = disk[front]
            if front_id is not None or space < n:
                continue
            if space > n:
                disk.insert(front + 1, (None, space - n))
                back += 1
            disk[front] = (id, n)
            disk[back] = (None, n)
            break
    return chain(*([i] * n for i, n in disk))


def part_2(file_name):
    return checksum(defrag_2(decompress_2(read_disk(file_name))))


if __name__ == "__main__":
    print("1. Example:", part_1("data/day09-example.txt"), "=? 1928")
    print("1. Answer:", part_1("data/day09-data.txt"))
    print("2. Example:", part_2("data/day09-example.txt"), "=? 2858")
    print("2. Answer:", part_2("data/day09-data.txt"))
