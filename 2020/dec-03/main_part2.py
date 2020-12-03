rows = []
with open("input.txt") as f:
    for line in f.read().split("\n"):
        rows.append([char for char in line])

directions = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

total_trees = 0
for direction in directions:
    [right, down] = direction
    x = y = trees = 0
    
    while y < len(rows):
        if rows[y][x] == '#':
            trees += 1

        x = (x + right) % 31
        y += down

    total_trees = (trees if total_trees == 0 else trees * trees)

print("# of trees:", total_trees)
