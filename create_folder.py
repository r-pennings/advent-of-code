import os

year = input("Please enter advent of code year:")

if not os.path.exists(year):
    os.makedirs(year)

for day in range(1, 26):
    day_folder = year + "/dec-{:02d}".format(day)
    if not os.path.exists(day_folder):
        os.makedirs(day_folder)
    
    if not os.path.exists(day_folder + "/main.py"):
        file = open(day_folder + "/main.py", "w+")

    if not os.path.exists(day_folder + "/input.txt"):
        file = open(day_folder + "/input.txt", "w+")

print("Succesfully created", year)