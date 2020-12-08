def find_accumulator(lines):
    accumulator = 0
    indices = []
    index = 0
    while index < len(lines):
        if index in indices:
            return None

        indices.append(index)

        op, val = lines[index].split()

        if op == 'nop':
            index += 1
        elif op == 'acc':
            accumulator += int(val)
            index += 1
        elif op == 'jmp':
            index += int(val)
    return accumulator


lines = [line.strip() for line in open("input.txt")]
print("accumulator", find_accumulator(lines))
