def process(path):
    coordinates = {}

    x = y = step = 0
    for move in path:
        moves = {'U': [0, 1], 'R': [1, 0], 'D': [0, -1], 'L': [-1, 0]}
        move_x, move_y = moves[move[0]]

        for _ in range(0, int(move[1:])):
            x += move_x
            y += move_y

            step += 1

            if (x, y) not in coordinates:
                coordinates[(x, y)] = step

    return coordinates


with open("input.txt") as f:
    paths = [line.split(',') for line in f]

path1 = process(paths[0])
path2 = process(paths[1])

intersections = set(path1.keys()).intersection(set(path2.keys()))

distances = [(abs(intersection[0]) + abs(intersection[1])) for intersection in intersections]

print("Shortest distance", min(distances))
