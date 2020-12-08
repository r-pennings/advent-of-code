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

alternates = [lines.index(line) for line in lines if 'jmp' in line or 'nop' in line]

accumulator = 0
for alt in alternates:
    temp_lines = lines.copy()
    line = lines[alt]

    if 'jmp' in line:
        temp_lines[alt] = "nop " + line.split()[1]
    elif 'nop' in line:
        temp_lines[alt] = "jmp " + line.split()[1]

    if find_accumulator(temp_lines):
        accumulator = find_accumulator(temp_lines)

print("accumulator", accumulator)