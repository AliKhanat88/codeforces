import sys
input = sys.stdin.readline

class DSU:
    def __init__(self, n):
        # Initialize parent and size arrays
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, a):
        # Find with path compression
        x = a
        while self.parent[x] != x:
            x = self.parent[x]
        while a != x:
            temp = self.parent[a]
            self.parent[a] = x
            a = temp
        return x

    def union(self, a, b):
        # Find roots of both nodes
        parent_a = self.find(a)
        parent_b = self.find(b)
        
        # If they are already in the same set, return False
        if parent_a == parent_b:
            return False
        
        # Union by size
        if self.size[parent_a] >= self.size[parent_b]:
            self.parent[parent_b] = parent_a
            self.size[parent_a] += self.size[parent_b]
        else:
            self.parent[parent_a] = parent_b
            self.size[parent_b] += self.size[parent_a]
        
        return True  # Union was successful


    
def solve():
    n, m = map(int, input().split())
    adj = [[] for i in range(n+1)]
    edges = [0] * m
    dsu = DSU(n)
    others = []
    for i in range(m):
        a, b = map(int, input().split())
        if dsu.union(a-1, b-1) == False:
            others.append((a, b))
            edges[i] = (a, b, "1")
        else:
            adj[a].append(b)
            adj[b].append(a)
            edges[i] = (a, b, "0")
    # print(others)
    if len(others) > 3:
        raise Exception()
    if len(others) <= 2:
        print("".join([num[2] for num in edges]))
        return
    can = True
    dsu2 = DSU(n)
    for edge in others:
        a, b = edge[0], edge[1]
        if dsu2.union(a-1, b-1) == False:
            can = False
            
    # print(can)
    if can:
        print("".join([num[2] for num in edges]))
        return
    
    remove_edge = others[0]
    edges[edges.index((remove_edge[0], remove_edge[1], "1"))] = (remove_edge[0], remove_edge[1], "0")
    # print(remove_edge)
    # print(edges)
    root = remove_edge[0]
    other_vertice = remove_edge[1]
    # print(root, other_vertice)
    dfs = [(root, -1)]
    for v, p in dfs:
        if v == other_vertice:
            # print(v, p, "in dfs")
            if (v, p, "0") in edges:
                edges[edges.index((v, p, "0"))] = (v, p, "1")
            elif (p, v, "0") in edges:
                edges[edges.index((p, v, "0"))] = (p, v, "1")
            break
        for child in adj[v]:
            if child != p:
                dfs.append((child, v))
    print("".join([num[2] for num in edges]))
    return





for t in range(int(input())):
    solve()