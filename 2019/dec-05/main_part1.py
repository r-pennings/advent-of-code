def process(mem):
    # no clue what this does, but fixed my problem
    mem = mem[:]

    idx = 0
    while idx < len(mem):
        opcode = mem[idx] % 100
        mode1 = 0
        mode2 = 0

        if mem[idx] >= 100:
            if (mem[idx] % 1000 - mem[idx] % 100) == 100:
                mode1 = 1
            
            if (mem[idx] % 10000 - mem[idx] % 1000) == 1000:
                mode2 = 1

        print(mode1, mode2)
        if opcode == 1:
            num1 = mem[mem[idx + 1]] if mode1 == 0 else mem[idx + 1]
            num2 = mem[mem[idx + 2]] if mode2 == 0 else mem[idx + 2]
            mem[mem[idx + 3]] = num1 + num2
            idx += 4
        elif opcode == 2:
            num1 = mem[mem[idx + 1]] if mode1 == 0 else mem[idx + 1]
            num2 = mem[mem[idx + 2]] if mode2 == 0 else mem[idx + 2]
            mem[mem[idx + 3]] = num1 * num2
            idx += 4
        elif opcode == 3:
            console_input = input("Input: ")
            if (len(console_input) != 0):
                mem[mem[idx + 1]] = int(console_input)

            idx += 2
        elif opcode == 4:
            print("Output:", mem[mem[idx + 1]])
            idx += 2
        elif opcode == 99:
            return mem
        else:
            idx += 2

    return mem

code = open("input.txt")
nums = [int(num) for num in code.read().split(',')]
code.close()

process(nums)
