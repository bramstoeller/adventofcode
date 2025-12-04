# Advent of Code 2024, Day 13
# https://adventofcode.com/2024/day/13


# Part One
import re

PATTERN = re.compile(r"[A-Za-z ]+: X[+=](\d+), Y[+=](\d+)")


def load_equations(file_name):
    data = open(file_name, "r").read()
    equations = data.split("\n\n")
    for eq in equations:
        a, b, p = eq.strip().split("\n")
        ax, ay = PATTERN.match(a).groups()
        bx, by = PATTERN.match(b).groups()
        px, py = PATTERN.match(p).groups()
        yield int(ax), int(ay), int(bx), int(by), int(px), int(py)


# Original solution:
# https://numpy.org/doc/2.1/reference/generated/numpy.linalg.solve.html
"""
import numpy as np

def solve_numpy(ax, ay, bx, by, px, py):
    buttons = np.array([[ax, bx], [ay, by]])
    price = np.array([px, py])
    a, b = np.linalg.solve(buttons, price)
    a = round(a)
    b = round(b)
    if a * ax + b * bx == px and a * ay + b * by == py:
        return 3 * a + b
    return 0
"""


# Manual solution:
# Cramer's Rule: https://en.wikipedia.org/wiki/Cramer%27s_rule
# a = det([[px, bx], [py, by]]) / det([[ax, bx], [ay, by]])
# b = det([[ax, px], [ay, py]]) / det([[ax, bx], [ay, by]])
#
# Determinant: https://en.wikipedia.org/wiki/Determinant
# The determinant of a 2x2 matrix is the product of the diagonal minus the product of the off-diagonal elements.
# det([[ax, bx], [ay, by]]) = ax * by - ay * bx
#
def solve(ax, ay, bx, by, px, py):
    det = ax * by - ay * bx
    det_a = px * by - py * bx
    det_b = ax * py - ay * px
    a = round(det_a / det)
    b = round(det_b / det)
    if a * ax + b * bx == px and a * ay + b * by == py:
        return 3 * a + b
    return 0


def part_1(file_name):
    return sum(solve(*eq) for eq in load_equations(file_name))


# Part Two
def part_2(file_name):
    equations = load_equations(file_name)
    equations = [
        ab + [px + 10000000000000, py + 10000000000000] for *ab, px, py in equations
    ]
    return sum(solve(*eq) for eq in equations)


if __name__ == "__main__":
    print("1. Example:", part_1("data/day13-example.txt"), "=? 480")
    print("1. Answer:", part_1("data/day13-data.txt"))
    print("2. Answer:", part_2("data/day13-data.txt"))
