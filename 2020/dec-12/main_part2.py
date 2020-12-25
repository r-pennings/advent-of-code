import math


def rotate(origin, point, angle):
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy


lines = [line.rstrip() for line in open("input.txt")]
coords = {"x": 0, "y": 0}
waypoint = {"x": 10, "y": 1}
for line in lines:
    direction, n = line[0], line[1:]
    n = int(n)

    if direction == "N":
        waypoint["y"] += n
    elif direction == "S":
        waypoint["y"] -= n
    elif direction == "E":
        waypoint["x"] += n
    elif direction == "W":
        waypoint["x"] -= n
    elif direction == "F":
        coords["x"] += waypoint["x"] * n
        coords["y"] += waypoint["y"] * n
    elif direction == "L" or direction == "R":
        if direction == "R":
            n = -n
        waypoint["x"], waypoint["y"] = rotate(
            (0, 0), (waypoint["x"], waypoint["y"]), math.radians(n)
        )

print("Distance:", int(abs(coords["x"]) + abs(coords["y"])))
