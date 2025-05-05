def tarjan(n,m, adj):
    visited = [False] * (n + 1)
    dis = [-1] * (n + 1)
    low = [-1] * (n + 1)
    idx = [0] * (n + 1)
    timer = 0
    bridges = 0
    stack = [(1, 0)]
    while stack:
        v, p = stack.pop()
        if v > 0:
            # It means it is forward edge
            if not visited[v]:
                dis[v] = low[v] = timer
                timer += 1
                visited[v] = True
            if idx[v] >= len(adj[v]):
                continue
            child = adj[v][idx[v]]
            idx[v] += 1
            stack.append((v, p))
            if child != p:
                if visited[child]:
                    low[v] = min(low[v], dis[child])
                else:
                    stack.append((-v, child))
                    stack.append((child, v))

        else:
            # it means it is a backward edge
            v, child = -v, p
            low[v] = min(low[v], low[child])
            if low[child] > dis[v]:
                # means cycle edge
                bridges += 1
    cycles_edges = m - bridges
    return bridges
