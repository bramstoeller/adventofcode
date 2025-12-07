# Advent of Code 2024, Day 17
# https://adventofcode.com/2024/day/17


# Part One


def boom():
    raise ValueError("Invalid combo operand")


combos = {
    0: lambda reg: 0,
    1: lambda reg: 1,
    2: lambda reg: 2,
    3: lambda reg: 3,
    4: lambda reg: reg[0],
    5: lambda reg: reg[1],
    6: lambda reg: reg[2],
    7: lambda reg: boom(),
}


# The adv instruction (opcode 0) performs division. The numerator is the value in the A register. The denominator is found by raising 2 to the power of the instruction's combo operand. (So, an operand of 2 would divide A by 4 (2^2); an operand of 5 would divide A by 2^B.) The result of the division operation is truncated to an integer and then written to the A register.
def adv(reg, op):
    reg[0] = reg[0] // (2 ** combos[op](reg))
    reg[-1] += 2


# The bxl instruction (opcode 1) calculates the bitwise XOR of register B and the instruction's literal operand, then stores the result in register B.
def bxl(reg, op):
    reg[1] = reg[1] ^ op
    reg[-1] += 2


# The bst instruction (opcode 2) calculates the value of its combo operand modulo 8 (thereby keeping only its lowest 3 bits), then writes that value to the B register.
def bst(reg, op):
    reg[1] = combos[op](reg) % 8
    reg[-1] += 2


# The jnz instruction (opcode 3) does nothing if the A register is 0. However, if the A register is not zero, it jumps by setting the instruction pointer to the value of its literal operand; if this instruction jumps, the instruction pointer is not increased by 2 after this instruction.
def jnz(reg, op):
    if reg[0] == 0:
        reg[-1] += 2
    else:
        reg[-1] = op


# The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C, then stores the result in register B. (For legacy reasons, this instruction reads an operand but ignores it.)
def bxc(reg, _):
    reg[1] = reg[1] ^ reg[2]
    reg[-1] += 2


# The out instruction (opcode 5) calculates the value of its combo operand modulo 8, then outputs that value. (If a program outputs multiple values, they are separated by commas.)
def out(reg, op):
    reg[-1] += 2
    return combos[op](reg) % 8


# The bdv instruction (opcode 6) works exactly like the adv instruction except that the result is stored in the B register. (The numerator is still read from the A register.)
def bdv(reg, op):
    reg[1] = reg[0] // (2 ** combos[op](reg))
    reg[-1] += 2


# The cdv instruction (opcode 7) works exactly like the adv instruction except that the result is stored in the C register. (The numerator is still read from the A register.)
def cdv(reg, op):
    reg[2] = reg[0] // (2 ** combos[op](reg))
    reg[-1] += 2


instructions = {0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv}


def load_program(file_name):
    data = open(file_name, "r").readlines()
    a = int(data[0].split(": ")[1])
    b = int(data[1].split(": ")[1])
    c = int(data[2].split(": ")[1])
    program = list(map(int, data[4].split(": ")[1].split(",")))
    return a, b, c, program


def fn_1(a, b, c, program):
    reg = [a, b, c, 0]
    output = []
    while 0 <= reg[-1] < len(program):
        cursor = reg[-1]
        opcode = program[cursor]
        operand = program[cursor + 1]
        instruction = instructions[opcode]
        result = instruction(reg, operand)
        if result is not None:
            output.append(result)
    return output


def part_1(file_name):
    return ",".join(map(str, fn_1(*load_program(file_name))))


# Part Two


def fn_2(a, b, c, program):
    reg = [a, b, c, 0]
    output = []
    while 0 <= reg[-1] < len(program):
        cursor = reg[-1]
        opcode = program[cursor]
        operand = program[cursor + 1]
        instruction = instructions[opcode]
        result = instruction(reg, operand)
        if result is not None:
            if result != program[len(output)]:
                return False
            output.append(result)
    return output == program


def part_2(file_name):
    a, b, c, program = load_program(file_name)
    a = 0
    while True:
        if a % 1000000 == 0:
            print(a)
        if fn_2(a, b, c, program):
            return a
        a += 1


if __name__ == "__main__":
    from utils import run

    run(part_1, "data/day17-example1.txt", expected="4,6,3,5,6,3,5,2,1,0")
    run(part_1, "data/day17-data.txt", expected="7,1,3,7,5,1,0,3,4")
    # part_2 takes too long to run
    # run(part_2, "data/day17-example2.txt", expected=117440)
    # run(part_2, "data/day17-data.txt")
