def is_valid(num):
    counters = {}
    for i in range(len(num)):
        if i > 0 and num[i] < num[i - 1]:
            return False
        if i > 0 and num[i] == num[i - 1]:
            if num[i] not in counters:
                counters[num[i]] = 0
            counters[num[i]] += 1
    return 1 in counters.values()


passwords = [pw for pw in map(str, range(264360, 746325)) if is_valid(pw)]

print("# of passwords:", len(passwords))
