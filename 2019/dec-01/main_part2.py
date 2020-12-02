# Take its mass, divide by three, round down, and subtract 2

sum_of_fuel = 0

with open("input.txt") as _file:
    for line in _file:
        fuel = int(line)
        
        while fuel > 0:
            fuel = fuel // 3 - 2
            sum_of_fuel += fuel if (fuel > 0) else 0

print("Sum of fuel:", sum_of_fuel)