# Advent of Code 2025, Day 10
# https://adventofcode.com/2025/day/10

State1 = tuple[bool, ...]  # '#' = true, '.' = false
Button = list[int]  # list of indices to toggle
Buttons = list[Button]  # list of buttons
State2 = tuple[tuple[int, ...], int]  # (joltages, button index)


def load_data(input_file: str):
    machines = open(input_file).read().strip().split("\n")
    for machine in machines:
        parts = machine.split()
        target = tuple(x == "#" for x in parts[0].strip("[").strip("]"))
        buttons = [list(map(int, x.strip("(").strip(")").split(","))) for x in parts[1:-1]]
        joltages = tuple(map(int, parts[-1].strip("{(}").strip("}").split(",")))
        yield target, buttons, joltages


# Part One
def find_path_1(start, goal, actions):
    open_set = {start}
    closed_set = set()
    came_from = dict()
    g = {start: 0}
    f = {start: distance_1(start, goal)}

    while open_set:
        current = min(open_set, key=lambda x: f[x])
        print(f"Current: {current}, f={f[current]}, g={g[current]}")
        if current == goal:
            return reconstruct_path(came_from, current)
        open_set.remove(current)
        closed_set.add(current)
        g_score = g[current] + 1
        for nb in get_neighbors_1(current, actions):
            d = distance_1(nb, goal)
            if d == float("inf"):
                continue
            if nb in closed_set:
                continue
            if nb not in open_set:
                open_set.add(nb)
            elif g_score >= g[nb]:
                continue
            came_from[nb] = current
            g[nb] = g_score
            f[nb] = g_score + d
    return None


def distance_1(current: State1, target: State1) -> float:
    return 1 if not all(c == t for c, t in zip(current, target)) else 0


def get_neighbors_1(current: State1, buttons: Buttons):
    return [apply_button_1(current, btn) for btn in buttons]


def apply_button_1(state: State1, btn: Button) -> State1:
    new_state = list(state)
    for i in btn:
        new_state[i] = not new_state[i]
    return tuple(new_state)


def reconstruct_path(came_from: dict, p):
    path = [p]
    while p in came_from:
        p = came_from[p]
        path.append(p)
    return list(reversed(path))


def part_1(input_file):
    machines = load_data(input_file)
    total = 0
    for target, buttons, _ in machines:
        start = tuple(False for _ in range(len(target)))
        program = find_path_1(start, target, buttons)
        total += len(program) - 1
    return total


# Part Two:
def find_path_2(start, goal, actions):
    open_set = {start}
    closed_set = set()
    g = {start: 0}
    f = {start: distance_2(start, goal, actions)}

    while open_set:
        current = min(open_set, key=lambda x: (f[x], -max(x[0])))
        if current == goal:
            return g[current]
        open_set.remove(current)
        closed_set.add(current)
        g_score = g[current]
        for nb, cost in get_neighbors_2(current, goal, actions):
            d = distance_2(nb, goal, actions)
            if d == float("inf"):
                continue
            if nb in closed_set:
                continue
            if nb not in open_set:
                open_set.add(nb)
            elif g_score >= g[nb]:
                continue
            g[nb] = g_score + cost
            f[nb] = g[nb] + d
    return None


def make_mask(buttons: Buttons, i0, i1, n) -> list[bool]:
    mask = [False] * n
    for btn in buttons[i0 : i1 + 1]:
        for i in btn:
            mask[i] = True
    return mask


def distance_2(current: State2, target: State2, buttons: Buttons) -> float:
    c_values, c_idx = current
    t_values, t_idx = target
    n = len(c_values)

    # if any of the current state values exceed the target values, return infinity
    if any(map(lambda c, t: c > t, c_values, t_values)):
        return float("inf")

    # if any of the current values do not match the target and there is no action left to change it, return infinity
    mask = make_mask(buttons, c_idx, t_idx, n)
    if any(not m and c != t for c, t, m in zip(c_values, t_values, mask)):
        return float("inf")

    # Return the maximum difference between target and current values
    return max((t - c) for c, t in zip(c_values, t_values))


def get_neighbors_2(current: State2, target: State2, buttons: Buttons):
    c_values, c_idx = current
    t_values, t_idx = target
    btn = buttons[c_idx]
    mask = make_mask(buttons, c_idx, c_idx, len(c_values))
    max_count = min(t - c for c, t, m in zip(c_values, t_values, mask) if m)
    for n in range(0, max_count + 1):
        yield (tuple(c + n if i in btn else c for i, c in enumerate(c_values)), c_idx + 1), n


def part_2(input_file):
    print("---")
    machines = load_data(input_file)
    total = 0
    for _, buttons, target in machines:
        start = (tuple(0 for _ in range(len(target))), 0)
        buttons = sorted(buttons, key=len, reverse=True)
        print(target, buttons, end=" ")
        n = find_path_2(start, (target, len(buttons)), buttons)
        total += n
        print(n)
    return total


if __name__ == "__main__":
    from utils import download_puzzle_input, run

    download_puzzle_input()
    # run(part_1, "data/day10-example.txt", expected=7)
    # run(part_1, "data/day10-data.txt", expected=425)
    run(part_2, "data/day10-example.txt", expected=33)
    run(part_2, "data/day10-data.txt", expected=15883)
