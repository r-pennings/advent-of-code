lines = [line.rstrip() for line in open("input.txt")]

bag_types = []
bags = {}
for line in lines:
    bag = " ".join(line.split(" ")[:2])

    if bag not in bag_types:
        bag_types.append(bag)

    start_idx = line.index("contain ") + len("contain ")
    contains = line[start_idx:-1]

    all_contains = [" ".join(c.split(" ")[:-1]) for c in contains.split(", ")]

    c_list = {}
    for c in all_contains:
        str_list = c.split(" ")
        key = " ".join(str_list[1:])
        value = str_list[0]
        c_list[key] = value

    all_contains = c_list

    if bag in all_contains:
        all_contains.update(bags[bag])

    bags[bag] = all_contains


def check_bag(bags, search_bag, current_bag):
    if current_bag == search_bag:
        return 1
    if current_bag not in bags:
        return 0
    else:
        return max([check_bag(bags, search_bag, bag) for bag in bags[current_bag].keys()])

found_bags = sum([check_bag(bags, "shiny gold", bag) for bag in bags.keys() if bag != "shiny gold"])

print("# of bags", found_bags)
