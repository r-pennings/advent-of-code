rows = []
with open("input.txt") as f:
    for line in f.read().split("\n"):
        rows.append([char for char in line])

x = y = trees = 0

while y < len(rows):
    if rows[y][x] == '#':
        trees += 1

    x = (x + 3) % 31
    y += 1

print("# of trees:", trees)
