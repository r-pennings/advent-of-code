# Take its mass, divide by three, round down, and subtract 2

with open("input.txt") as _file:
    sum_of_fuel = sum([int(line) // 3 - 2 for line in _file])

print("Sum of fuel:", sum_of_fuel)