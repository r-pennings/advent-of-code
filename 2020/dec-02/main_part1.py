import re

valid_passwords = 0
with open("input.txt") as _file:
    for line in _file:
        [requirements, password] = [part.strip() for part in line.split(':')]
        [r_min, r_max, r_char] = [int(i) if i.isdigit() else i for i in re.split('-| ', requirements)]

        nr_of_chars = 0
        for char in password:
            if char == r_char:
                nr_of_chars += 1

        if r_min <= nr_of_chars <= r_max:
            valid_passwords += 1

print("# of valid passwords: ", valid_passwords)
