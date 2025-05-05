from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def solve():
    n, q = map(int, input().split())
    arr = [0] + list(map(int, input().split()))
    adj = [[] for i in range(n+1)]
    for i in range(n-1):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    
    org_adj = [[] for i in range(n+1)]
    parent = [0] * (n+1)
    visited = [False] * (n+1)
    importance = [0] * (n+1)
    childs = [0] * (n+1)
    dfs = [(1, 0)]
    for v, p in dfs:
        parent[v] = p
        visited[v] = True
        for child in adj[v]:
            if not visited[child]:
                dfs.append((child, v))

    for v, p in dfs[::-1]:
        if len(org_adj[v]) == 0:
            heappush(org_adj[p], (-1, v))
            importance[v] = arr[v]
            childs[v] = 1
            continue
        imp = arr[v]
        chil = 1
        for child in org_adj[v]:
            chil += childs[child[1]]
            imp += importance[child[1]]
        heappush(org_adj[p], (-chil, v))
        importance[v] = imp
        childs[v] = chil
    
    # print(org_adj)
    # print(importance)
    # print(childs)

    for i in range(q):
        type, vertice = map(int, input().split())
        if type == 1:
            print(importance[vertice])
        else:
            if childs[vertice] == 1:
                continue
            f_f = parent[vertice]
            f = vertice
            c = None
            while len(org_adj[f]) > 0:
                if parent[org_adj[f][0][1]] == f:
                    c = org_adj[f][0][1]
                    break
                else:
                    heappop(org_adj[f])
            assert c != None
            importance[f] -= importance[c]
            childs[f] -= childs[c]
            childs[c] += childs[f]
            importance[c] += importance[f]
            parent[c] = f_f
            parent[f] = c
            heappop(org_adj[f])
            heappush(org_adj[f_f], (-childs[c], c))
            heappush(org_adj[c], (-childs[f], f))
        




        






solve()