import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    graph = [[] for i in range(n + 1)]

    for i in range(m):
        a, b, w = map(int, input().split())

        graph[a].append((b, w))
        graph[b].append((a, w))

    
    print(graph)

    visited = [False] * (n + 1)
    idx = [0] * (n + 1)
    intime = [0] * (n + 1)
    outtime = [0] * (n + 1)
    stack = []
    timer = [0]
    ans = []
    def dfs(node):
        stack.append((node, -1, 9999999999999999999))

        while len(stack):
            print(stack)
            v, p, w = stack.pop()
            if v > 0:
                if not visited[v]:
                    visited[v] = True
                    intime[v] = outtime[v] = timer[0]
                    timer[0] += 1
                if idx[v] >= len(graph[v]):
                    continue
                child = graph[v][idx[v]][0]
                weight = graph[v][idx[v]][1]
                idx[v] += 1
                stack.append((v, p, w))
                if child == p:
                    continue
                if visited[child]:
                    outtime[v] = min(outtime[v], outtime[child])
                    ans.append((v, child, weight))
                else:
                    stack.append((-v, child, weight))
                    stack.append((child, v, weight))

            else:
                v, c, w = -v, p, w
                outtime[v] = min(outtime[v], outtime[c])
                if intime[v] > outtime[c]:
                    ans.append((v, c, w))

    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)
    print(intime)
    print(outtime)
    print(ans)
    mini = 9999999999999999999999
    edge = None
    for num in ans:
        if num[2] < mini:
            mini = ans[2]
            edge = num
    
    assert edge != None

    visited = [False] * (n + 1)
    stack = [(edge[1], edge[0])]

    parent = [0] * (n+1)
    parent[]
    while stack:
        cur = stack.pop()



for t in range(int(input())):
    solve()