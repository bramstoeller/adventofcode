# Advent of Code 2024, Day 9
# https://adventofcode.com/2024/day/9


# Part One
def load_data(file_name):
    return open(file_name, "r").read().strip()

def decompress(line):
    return [(int(i) // 2) if int(i) % 2 == 0 else None for i, n in enumerate(line.strip()) for _ in range(int(n))]


def compact(line):
    comp = []
    n = len(line)
    i = 0
    j = 0
    while i < n - j:
        if line[i] is not None:
            comp.append(line[i])
        else:
            while line[-(j+1)] is None:
                j += 1
            if i + j >= n:
                break
            comp.append(line[-(j+1)])
            j += 1
        i += 1
    return comp

def checksum(data):
    x = 0
    i = 0
    for n in data:
        if n is not None:
            x += i * int(n)
        i += 1
    return x

def part_1(file_name):
    return checksum(compact(decompress(load_data(file_name))))


# Part Two
def load_data2(file_name):
    return open(file_name, "r").read().strip()

def decompress2(line):
    dec = [((int(i) // 2, int(n))) if int(i) % 2 == 0 else (None, int(n)) for i, n in enumerate(line.strip())]
    return [x for x in dec if x[1] > 0]


def compact2(line):
    back = len(line) - 1
    while back > 0:
        id, n = line[back]
        if id is None:
            back -= 1
            continue
        for front in range(back):
            id_, n_ = line[front]
            if id_ is not None:
                continue
            if n_ < n:
                continue
            if n_ == n:
                line[front] = (id, n)
                line[back] = (None, n)
                break
            if n_ > n:
                line[front] = (id, n)
                line[back] = (None, n)
                line.insert(front + 1, (None, n_ - n))
                back += 1
                break
        back -= 1


    out = []
    for i, n in line:
        out += [i] * n
    return out


def part_2(file_name):
    return checksum(compact2(decompress2(load_data2(file_name))))

if __name__ == "__main__":
    print("1. Example:", part_1("data/day09-example.txt"), "=? 1928")
    print("1. Answer:", part_1("data/day09-data.txt"))
    print("2. Example:", part_2("data/day09-example.txt"), "=? 2858")
    print("2. Answer:", part_2("data/day09-data.txt"))
