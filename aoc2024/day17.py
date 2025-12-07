# Advent of Code 2024, Day 17
# https://adventofcode.com/2024/day/17
from dataclasses import dataclass


@dataclass
class Reg:
    A: int
    B: int
    C: int
    idx: int


# Part One


def boom():
    raise ValueError("Invalid combo operand")


combos = {
    0: lambda reg: 0,
    1: lambda reg: 1,
    2: lambda reg: 2,
    3: lambda reg: 3,
    4: lambda reg: reg.A,
    5: lambda reg: reg.B,
    6: lambda reg: reg.C,
    7: lambda reg: boom(),
}


# The adv instruction (opcode 0) performs division. The numerator is the value in the A register. The denominator is
# found by raising 2 to the power of the instruction's combo operand. (So, an operand of 2 would divide A by 4 (2^2);
# an operand of 5 would divide A by 2^B.) The result of the division operation is truncated to an integer and then
# written to the A register.
def adv(reg: Reg, op: int):
    reg.A = reg.A >> combos[op](reg)
    reg.idx += 2


# The bxl instruction (opcode 1) calculates the bitwise XOR of register B and the instruction's literal operand, then
# stores the result in register B.
def bxl(reg: Reg, op: int):
    reg.B = reg.B ^ op
    reg.idx += 2


# The bst instruction (opcode 2) calculates the value of its combo operand modulo 8 (thereby keeping only its lowest
# 3 bits), then writes that value to the B register.
def bst(reg: Reg, op: int):
    reg.B = combos[op](reg) % 8
    reg.idx += 2


# The jnz instruction (opcode 3) does nothing if the A register is 0. However, if the A register is not zero, it jumps
# by setting the instruction pointer to the value of its literal operand; if this instruction jumps, the instruction
# pointer is not increased by 2 after this instruction.
def jnz(reg: Reg, op: int):
    if reg.A == 0:
        reg.idx += 2
    else:
        reg.idx = op


# The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C, then stores the result in
# register B. (For legacy reasons, this instruction reads an operand but ignores it.)
def bxc(reg, _):
    reg.B = reg.B ^ reg.C
    reg.idx += 2


# The out instruction (opcode 5) calculates the value of its combo operand modulo 8, then outputs that value. (If a
# program outputs multiple values, they are separated by commas.)
def out(reg: Reg, op: int):
    reg.idx += 2
    return combos[op](reg) % 8


# The bdv instruction (opcode 6) works exactly like the adv instruction except that the result is stored in the
# B register. (The numerator is still read from the A register.)
def bdv(reg: Reg, op: int):
    reg.B = reg.A >> combos[op](reg)
    reg.idx += 2


# The cdv instruction (opcode 7) works exactly like the adv instruction except that the result is stored in the
# C register. (The numerator is still read from the A register.)
def cdv(reg: Reg, op: int):
    reg.C = reg.A >> combos[op](reg)
    reg.idx += 2


instructions = {0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv}


def load_program(file_name):
    data = open(file_name, "r").readlines()
    a = int(data[0].split(": ")[1])
    b = int(data[1].split(": ")[1])
    c = int(data[2].split(": ")[1])
    program = list(map(int, data[4].split(": ")[1].split(",")))
    return a, b, c, program


def run_program(a, b, c, program):
    reg = Reg(a, b, c, 0)
    output = []
    while 0 <= reg.idx < len(program):
        cursor = reg.idx
        opcode = program[cursor]
        operand = program[cursor + 1]
        instruction = instructions[opcode]
        result = instruction(reg, operand)
        if result is not None:
            output.append(result)
    return output


def part_1(file_name):
    return ",".join(map(str, run_program(*load_program(file_name))))


# Part Two
def find_a(b, c, program):
    # The final A should be 0 in order to end the program
    A = [0]

    # Try to recreate the last program's 3-bit value (operand) first,
    # then the second to last 3-bit value (opcode), etc.
    for target in reversed(program):
        # In the previous step (A << 3) there are 8 options (0-7)
        # Try each option to see if it would result in the target output
        # Use the candidates to generate the next target.
        A = [(a << 3) + i for a in A for i in range(8) if run_program((a << 3) + i, b, c, program)[0] == target]

    # When done, find the smallest candidate
    return min(A)


def part_2(file_name):
    _, b, c, program = load_program(file_name)
    return find_a(b, c, program)


if __name__ == "__main__":
    from utils import run

    run(part_1, "data/day17-example1.txt", expected="4,6,3,5,6,3,5,2,1,0")
    run(part_1, "data/day17-data.txt", expected="7,1,3,7,5,1,0,3,4")
    run(part_2, "data/day17-example2.txt", expected=117440)
    run(part_2, "data/day17-data.txt", expected=190384113204239)
