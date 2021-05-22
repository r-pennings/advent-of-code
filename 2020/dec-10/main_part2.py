lines = [int(line.strip()) for line in open("input_test.txt")]

lines.append(max(lines) + 3)

jolts = {1: 0, 2: 0, 3: 0}
num = min(lines)
jolts[num] += 1
while num < max(lines):
    for i in range(1, 4):
        sum = num + i
        if sum in lines:
            jolts[i] += 1
            num = sum
            break
        
print("number =", (jolts[1] * jolts[3]))
