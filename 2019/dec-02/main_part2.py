def process(input):
    # no clue what this does, but fixed my problem
    input = input[:]
    
    index = 0
    while index < len(input):
        operator = input[index]
        number1 = input[input[index + 1]]
        number2 = input[input[index + 2]]
        nr_index = input[index + 3]

        if operator == 99:
            return input[0]
        elif operator == 1:
            input[nr_index] = number1 + number2
        elif operator == 2:
            input[nr_index] = number1 * number2

        index += 4

    return input[0]


with open("input.txt") as f:
    nums = [int(i) if i.isdigit() else i for i in f.read().split(',')]

for noun in range(100):
    for verb in range(100):
        nums[1] = noun
        nums[2] = verb

        output = process(nums)

        if output == 19690720:
            print("Output:", 100 * noun + verb)
            break
