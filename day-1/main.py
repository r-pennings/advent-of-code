numbers = []

number_file = open("numbers.txt", "r")

for line in number_file.readlines():
    numbers.append(int(line))

first_nr = 0
second_nr = 0

for first_idx, first in enumerate(numbers):
    for second_idx, second in enumerate(numbers[first_idx+1:]):
        if first + second == 2020:
            print("{} + {} = {}".format(first, second, (first + second)))
            first_nr = first
            second_nr = second

print("{} * {} = {}".format(first_nr, second_nr, (first_nr * second_nr)))

first_nr = 0
second_nr = 0
third_nr = 0

for first_idx, first in enumerate(numbers):
    for second_idx, second in enumerate(numbers[first_idx+1:]):
        for third_idx, third in enumerate(numbers[second_idx+1:]):
            if first + second + third == 2020:
                print("{} + {} + {} = {}".format(first, second, third, (first + second + third)))
                first_nr = first
                second_nr = second
                third_nr = third

print("{} * {} * {} = {}".format(first_nr, second_nr, third_nr, (first_nr * second_nr * third_nr)))