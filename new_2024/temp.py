def generate_random_tree(n, weighted=False, weight_range=(1, 100)):
    nodes = list(range(1, n + 1))
    random.shuffle(nodes)
    edges = []
    in_tree = {nodes[0]}  # Start from a random node
    remaining = set(nodes[1:])
    while remaining:
        u = random.choice(list(in_tree))
        v = remaining.pop()
        w = random.randint(*weight_range) if weighted else None
        edges.append((u, v, w) if weighted else (u, v))
        in_tree.add(v)
    return edges