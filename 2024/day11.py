# Advent of Code 2024, Day 11
# https://adventofcode.com/2024/day/11


# Part One
def load_data(file_name):
    return list(map(int, open(file_name, "r").read().strip().split()))


def blink(stones):
    out = []
    for s in stones:
        if s == 0:
            out.append(1)
        elif len(str(s)) % 2 == 0:
            x = str(s)
            out.append(int(x[:len(x) // 2]))
            out.append(int(x[len(x) // 2:]))
        else:
            out.append(s * 2024)
    return out


def part_1(file_name, n=25):
    stones = load_data(file_name)
    for i in range(n):
        stones = blink(stones)
    return len(stones)


# Part Two

def blinky(stones):
    for s in stones:
        if s == 0:
            yield 1
        elif len(str(s)) % 2 == 0:
            x = str(s)
            yield int(x[:len(x) // 2])
            yield int(x[len(x) // 2:])
        else:
            yield s * 2024

cache = {}

def recurse(stones, n):
    if n == 0:
        return len(stones)
    total = 0
    for s in blinky(stones):
        if (s, n-1) not in cache:
            cache[(s, n-1)] = recurse([s], n-1)
        total += cache[(s, n-1)]
    return total


def part_2(file_name, n=75):
    stones = load_data(file_name)
    return recurse(stones, n)


if __name__ == "__main__":
    print("1. Example:", part_1("data/day11-example.txt"), "=? 55312")
    print("1. Answer:", part_1("data/day11-data.txt"))
    print("2. Example:", part_2("data/day11-example.txt", 25), "=? 55312")
    print("2. Answer:", part_2("data/day11-data.txt"))
