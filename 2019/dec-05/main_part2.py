from enum import Enum


class Operation(Enum):
    ADDITION = 1
    MULTIPLICATION = 2
    INPUT = 3
    OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    TERMINATION = 99


class Mode(Enum):
    POSITION = 0
    IMMEDIATE = 1


def process(mem):
    idx = 0
    while mem[idx] != Operation.TERMINATION.value:
        opcode = Operation(mem[idx] % 100)
        mode1 = Mode.POSITION
        mode2 = Mode.POSITION

        if mem[idx] >= 100:
            if (mem[idx] % 1000 - mem[idx] % 100) == 100:
                mode1 = Mode.IMMEDIATE
            if (mem[idx] % 10000 - mem[idx] % 1000) == 1000:
                mode2 = Mode.IMMEDIATE

        if opcode is Operation.ADDITION:
            num1 = mem[idx + 1] if mode1 is Mode.IMMEDIATE else mem[mem[idx + 1]]
            num2 = mem[idx + 2] if mode2 is Mode.IMMEDIATE else mem[mem[idx + 2]]
            mem[mem[idx + 3]] = num1 + num2
            idx += 4
        elif opcode is Operation.MULTIPLICATION:
            num1 = mem[idx + 1] if mode1 is Mode.IMMEDIATE else mem[mem[idx + 1]]
            num2 = mem[idx + 2] if mode2 is Mode.IMMEDIATE else mem[mem[idx + 2]]
            mem[mem[idx + 3]] = num1 * num2
            idx += 4
        elif opcode is Operation.INPUT:
            console_input = input("Input: ")
            mem[mem[idx + 1]] = int(console_input)
            idx += 2
        elif opcode is Operation.OUTPUT:
            print("Output:", mem[mem[idx + 1]])
            idx += 2
        elif opcode is Operation.JUMP_IF_TRUE:
            num1 = mem[idx + 1] if mode1 is Mode.IMMEDIATE else mem[mem[idx + 1]]
            num2 = mem[idx + 2] if mode2 is Mode.IMMEDIATE else mem[mem[idx + 2]]
            if num1 != 0:
                idx = num2
            else:
                idx += 3
        elif opcode is Operation.JUMP_IF_FALSE:
            num1 = mem[idx + 1] if mode1 is Mode.IMMEDIATE else mem[mem[idx + 1]]
            num2 = mem[idx + 2] if mode2 is Mode.IMMEDIATE else mem[mem[idx + 2]]
            if num1 == 0:
                idx = num2
            else:
                idx += 3
        elif opcode is Operation.LESS_THAN:
            num1 = mem[idx + 1] if mode1 is Mode.IMMEDIATE else mem[mem[idx + 1]]
            num2 = mem[idx + 2] if mode2 is Mode.IMMEDIATE else mem[mem[idx + 2]]
            mem[mem[idx + 3]] = 1 if num1 < num2 else 0
            idx += 4
        elif opcode is Operation.EQUALS:
            num1 = mem[idx + 1] if mode1 is Mode.IMMEDIATE else mem[mem[idx + 1]]
            num2 = mem[idx + 2] if mode2 is Mode.IMMEDIATE else mem[mem[idx + 2]]
            mem[mem[idx + 3]] = 1 if num1 == num2 else 0
            idx += 4

    print("halt")


with open("input.txt") as f:
    nums = [int(num) for num in f.read().split(',')]

process(nums)
