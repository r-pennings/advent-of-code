with open("input.txt") as _file:
    for line in _file:
        ups = len(line.split('('))
        downs = len(line.split(')'))
        print("Floor #: " + str(ups - downs))

_file.close()
