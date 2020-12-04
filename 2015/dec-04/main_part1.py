import hashlib

input_string = "iwrupvqb"

num = 0
while True:
    check_string = input_string + str(num)
    hashed = hashlib.md5(check_string.encode()).hexdigest()
    if hashed[:5] == '00000':
        break

    num += 1

print("Index", num)