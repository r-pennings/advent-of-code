lines = [line.strip() for line in open("input.txt")]

grid = []
for x in range(0, 1000):
    grid.append([])
    for y in range(0, 1000):
        grid[x].append(0)

for line in lines:
    s = line

    operation = None
    if line.startswith('toggle'):
        s = line[len('toggle '):]
        operation = 0
    elif line.startswith('turn off'):
        s = line[len('turn off '):]
        operation = 1
    elif line.startswith('turn on'):
        s = line[len('turn on '):]
        operation = 2
    
    splitted = s.split(' ')
    start_x, start_y = splitted[0].split(',')
    end_x, end_y = splitted[2].split(',')

    for x in range(int(start_x), int(end_x)):
        for y in range(int(start_y), int(end_y)):
            if (operation == 0 and grid[x][y] == 1) or operation == 1:
                grid[x][y] = 0
            
            if (operation == 0 and grid[x][y] == 0) or operation == 2:
                grid[x][y] = 1

lights = 0
for x in range(0, 1000):
    for y in range(0, 1000):
        if grid[x][y] == 1:
            lights += 1
print("# of lit lights", lights)
