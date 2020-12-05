lines = [line.strip() for line in open("input.txt")]


def is_valid(string):
    if sum(1 for c in string if c in 'aeiou') < 3:
        return False
    has_repeat = False
    for i in range(1, len(string)):
        if string[i - 1] == string[i]:
            has_repeat = True
    if not has_repeat:
        return False
    if sum(1 for x in ['ab', 'cd', 'pq', 'xy'] if x in string) > 0:
        return False
    return True


valid_strings = [line for line in lines if is_valid(line)]

print("# of valid strings", len(valid_strings))
