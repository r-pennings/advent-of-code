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


def count_contents(color, children_graph):
    return sum(count + count * count_contents(child_color, children_graph)
               for child_color, count in children_graph[color])


_, children = parse("input_test.txt")
print(f"{count_contents('shiny gold', children)} bags are in a 'shiny gold'.")
