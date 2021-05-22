lines = [line for line in open("input.txt").read().split(", ")]

location = [0, 0]
deg = 0
for line in lines:
    if line[:1] == 'R':
        deg = (deg + 90 if deg < 270 else 0)
    elif line[:1] == 'L':
        deg = (deg - 90 if deg > 0 else 270)

    if deg == 0:
        location[1] += int(line[1:])
    elif deg == 90:
        location[0] += int(line[1:])
    elif deg == 180:
        location[1] -= int(line[1:])
    elif deg == 270:
        location[0] -= int(line[1:])

print("Blocks: " + str(abs(int(location[0])) + abs(int(location[1]))))
