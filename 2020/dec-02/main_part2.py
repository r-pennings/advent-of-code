import re

valid_passwords = 0
with open("input.txt") as _file:
    for line in _file:
        [requirements, password] = [part.strip() for part in line.split(':')]
        [r_pos1, r_pos2, r_char] = [int(i) if i.isdigit() else i for i in re.split('-| ', requirements)]

        if bool(password[r_pos1 - 1] == r_char) ^ bool(password[r_pos2 - 1] == r_char):
            valid_passwords += 1

print("# of valid passwords: ", valid_passwords)
