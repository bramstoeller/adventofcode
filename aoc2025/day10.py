# Advent of Code 2025, Day 10
# https://adventofcode.com/2025/day/10

import numpy as np
from scipy.optimize import milp, LinearConstraint


def load_data(input_file: str):
    machines = open(input_file).read().strip().split("\n")
    for machine in machines:
        parts = machine.split()
        target = tuple(x == "#" for x in parts[0].strip("[").strip("]"))
        buttons = [list(map(int, x.strip("(").strip(")").split(","))) for x in parts[1:-1]]
        joltages = tuple(map(int, parts[-1].strip("{(}").strip("}").split(",")))
        yield target, buttons, joltages


# Part One
def distance(current, target):
    return sum(s != t for s, t in zip(current, target)) / len(current)


def get_neighbors(current, buttons):
    return [(apply_button(current, btn), btn) for btn in buttons]


def apply_button(state, btn):
    new_state = list(state)
    for i in btn:
        new_state[i] = not new_state[i]
    return tuple(new_state)

def reconstruct_path(came_from, p):
    path = [(p, None)]
    while p in came_from:
        p, a = came_from[p]
        path.append((p, a))
    return list(reversed(path))


def find_path(start, goal, actions):
    open_set = {start}
    closed_set = set()
    came_from = dict()
    g = {start: 0}
    f = {start: distance(start, goal)}

    while open_set:
        current = min(open_set, key=lambda x: f[x])
        if current == goal:
            return reconstruct_path(came_from, current)
        open_set.remove(current)
        closed_set.add(current)
        g_score = g[current] + 1
        for nb, act in get_neighbors(current, actions):
            d = distance(nb, goal)
            if d == float("inf"):
                continue
            if nb in closed_set:
                continue
            if nb not in open_set:
                open_set.add(nb)
            elif g_score >= g[nb]:
                continue
            came_from[nb] = (current, act)
            g[nb] = g_score
            f[nb] = g_score + d
    return None


def part_1(input_file):
    machines = load_data(input_file)
    total = 0
    for target, buttons, _ in machines:
        start = tuple(False for _ in range(len(target)))
        program = find_path(start, target, buttons)
        total += len(program) - 1
    return total


# Part Two: https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.milp.html
def part_2(input_file):
    machines = load_data(input_file)
    total = 0
    for _, buttons, joltages in machines:
        n, m = len(buttons), len(joltages)
        A = np.array([[int(b in btn) for b in range(m)] for btn in buttons]).T
        target = np.array(joltages)
        result = milp(
            c=np.ones(n),
            constraints=[LinearConstraint(A, lb=target, ub=target)],
            integrality=1
        )
        presses = np.round(result.x).astype(int)
        total += sum(presses)
    return total


if __name__ == "__main__":
    from utils import download_puzzle_input, run

    download_puzzle_input()
    run(part_1, "data/day10-example.txt", expected=7)
    run(part_1, "data/day10-data.txt", expected=425)
    run(part_2, "data/day10-example.txt", expected=33)
    run(part_2, "data/day10-data.txt", expected=15883)
