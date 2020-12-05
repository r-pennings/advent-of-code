def process(string, minimum, maximum):
    mi, ma = minimum, maximum
    for c in string:
        if c == "F" or c == "L":
            ma = (mi + ma) // 2
        elif c == "B" or c == "R":
            mi = (mi + ma) // 2 + 1

    if mi == ma:
        return mi


lines = [line.strip() for line in open("input.txt")]
seats = [process(line[:-3], 0, 127) * 8 + process(line[-3:], 0, 7) for line in lines]
my_seat = [seat+1 for seat in seats if seat+1 not in seats and seat+2 in seats][0]
print("seat", my_seat)
