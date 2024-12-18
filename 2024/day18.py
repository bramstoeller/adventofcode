# Advent of Code 2024, Day 18
# https://adventofcode.com/2024/day/18


# Part One
def load_obstacles(file_name):
    data = open(file_name, "r").readlines()
    return list(tuple(map(int, line.split(","))) for line in data)

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_neighbors(node, size):
    x, y = node
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    return {(x + dx, y + dy) for dx, dy in d if 0 <= x + dx <= size and 0 <= y + dy <= size}


def reconstruct_path(came_from, p):
    path = [p]
    while p in came_from:
        p = came_from[p]
        path.append(p)
    return list(reversed(path))

def find_path(size, obstacles, start, goal):
    open_set = {start}
    closed_set = set(obstacles.copy())
    came_from = dict()
    g = {start: 0}
    f = {start: manhattan_distance(start, goal)}

    while open_set:
        current = min(open_set, key=lambda x: f[x])
        if current == goal:
            return reconstruct_path(came_from, current)
        open_set.remove(current)
        closed_set.add(current)
        g_score = g[current] + 1
        for nb in get_neighbors(current, size):
            if nb in closed_set:
                continue
            if nb not in open_set:
                open_set.add(nb)
            elif g_score >= g[nb]:
                continue
            came_from[nb] = current
            g[nb] = g_score
            f[nb] = g_score + manhattan_distance(nb, goal)
    return []


def print_shortest_path(size, obstacles, start, goal, path):
    for y in range(size + 1):
        for x in range(size + 1):
            if (x, y) in obstacles:
                print("#", end="")
            elif (x, y) == start:
                print("S", end="")
            elif (x, y) == goal:
                print("G", end="")
            elif (x, y) in path:
                print("O", end="")
            else:
                print(".", end="")
        print()


def part_1(file_name, size, n):
    obstacles = load_obstacles(file_name)[:n]
    start = (0, 0)
    goal = (size, size)
    shortest_path = find_path(size, obstacles, start, goal)
    # print_shortest_path(size, obstacles, start, goal, shortest_path)
    return len(shortest_path) - 1


# Part Two

def part_2(file_name, size, n0):
    obstacles = load_obstacles(file_name)
    start = (0, 0)
    goal = (size, size)
    shortest_path = find_path(size, obstacles[:n0], start, goal)
    for n in range(n0, len(obstacles)):
        if obstacles[n] in shortest_path:
            shortest_path = find_path(size, obstacles[:n + 1], start, goal)
        if not shortest_path:
            return ",".join(map(str, obstacles[n]))


if __name__ == "__main__":
    print("1. Example:", part_1("data/day18-example1.txt", 6, 12), "=? 22")
    print("1. Answer:", part_1("data/day18-data.txt", 70, 1024))
    print("2. Answer:", part_2("data/day18-data.txt", 70, 1024))
