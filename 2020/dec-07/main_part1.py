def parse(filename):
    parents = dict()
    children = dict()

    with open(filename, "r") as f:
        lines = f.readlines()

    # Figure out which colors we have
    for line in lines:
        color = " ".join(line.split()[:2])
        parents[color] = []
        children[color] = []

    # Fill in the digraphs
    for line in lines:
        words = line.split()
        if "no other" in line:
            continue

        parent_color = " ".join(words[:2])

        child_words = iter(words[4:])
        while True:
            count = int(next(child_words))
            child_adj = next(child_words)
            child_color = next(child_words)
            child_name = f"{child_adj} {child_color}"
            parents[child_name].append(parent_color)
            children[parent_color].append((child_name, count))
            if next(child_words)[-1] == ".":
                break

    return parents, children


def holders(color, parents_graph):
    result = set(parents_graph[color])
    for c in parents_graph[color]:
        result |= holders(c, parents_graph)
    return result


parents, _ = parse("input.txt")
gold_holders = len(holders("shiny gold", parents))
print(f"{gold_holders} different colors can contain 'shiny gold.'")
