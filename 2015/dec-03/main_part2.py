NORTH = '^'
EAST = '>'
SOUTH = 'v'
WEST = '<'

grid = ['0,0']
pos_santa = [0, 0]
pos_robo = [0, 0]
with open("input.txt") as _file:
    directions = _file.read()

    for x in range(len(directions)):
        direction = directions[x]

        santa = pos_robo if x % 2 == 0 else pos_santa
            
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

        if x % 2 == 0:
            pos_robo = santa
        else:
            pos_santa = santa 

print("# of houses: ", len(grid))
