NORTH = '^'
EAST = '>'
SOUTH = 'v'
WEST = '<'

grid = ['0,0']
position = [0, 0]
with open("input.txt") as _file:
    for line in _file:
        for direction in line:
            santa = position

            if direction == NORTH:
                santa = [santa[0], santa[1] - 1]
            elif direction == EAST:
                santa = [santa[0] + 1, santa[1]]
            elif direction == SOUTH:
                santa = [santa[0], santa[1] + 1]
            elif direction == WEST:
                santa = [santa[0] - 1, santa[1]]

            if not "{},{}".format(santa[0], santa[1]) in grid:
                grid.append("{},{}".format(santa[0], santa[1]))

            position = santa

print("# of houses: ", len(grid))
