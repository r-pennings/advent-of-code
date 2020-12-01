floor = 0
current_index = 0
basement = False

with open("input.txt") as _file:
    for line in _file:
        for char in line:
            if char == '(':
                floor += 1
            elif char == ')':
                floor -= 1
            else:
                print('invalid input')

            current_index += 1

            if floor < 0 and not basement:
                basement = True
                print("Entered basement at char: " + str(current_index))

    print("Floor #: " + str(floor))

_file.close()
