lines = [line.strip() for line in open("input.txt")]


def has_two_pair(string):
    for i in range(1, len(string)):
        s = string[i-1] + string[i]
        if s in string[i+1:]:
            return True
    return False


def has_split(string):
    for i in range(2, len(string)):
        if string[i-2] == string[i]:
            return True
    return False

valid_strings = [line for line in lines if has_two_pair(line) and has_split(line)]

print("# of valid strings", len(valid_strings))
