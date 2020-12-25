lines = [line.rstrip() for line in open("input.txt")]

dirs = ["N", "E", "S", "W"]

current_direction = "E"
current_distance = {"N": 0, "E": 0, "S": 0, "W": 0}
for line in lines:
    direction, n = line[0], line[1:]
    n = int(n)

    if direction == "F":
        current_distance[current_direction] += n

    if direction == "R":
        i = int(n) // 90
        ndir = (dirs.index(current_direction) + i) % len(dirs)
        current_direction = dirs[ndir]

    if direction == "L":
        i = int(n) // 90
        ndir = (dirs.index(current_direction) - i) % len(dirs)
        current_direction = dirs[ndir]

    if direction in ["N", "E", "S", "W"]:
        current_distance[direction] += n

dX = current_distance["E"] - current_distance["W"]
dY = current_distance["N"] - current_distance["S"]

print("Distance:", abs(dX) + abs(dY))
