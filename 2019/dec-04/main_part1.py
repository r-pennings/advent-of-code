def is_valid(num):
    has_doubles = False
    for i in range(len(num)):
        if i > 0 and num[i] < num[i - 1]:
            return False
        if i > 0 and num[i] == num[i - 1]:
            has_doubles = True
    return has_doubles


passwords = [pw for pw in map(str, range(264360, 746325)) if is_valid(pw)]

print("# of passwords:", len(passwords))
