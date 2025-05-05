import sys
input = sys.stdin.readline
from heapq import heappop, heappush


def solve():
    n, m = map(int, input().split())
    t0, t1, t2 = map(int, input().split())

    graph = [[] for i in range(n+1)]
    for i in range(m):
        u, v, l1, l2 = map(int, input().split())
        graph[u].append((v, l1, l2))
        graph[v].append((u, l1, l2))
    
    def check(start):
        heap = [(start, 1)]
        visited = [False] * (n+1)
        while len(heap) != 0:
            cur = heappop(heap)
            if visited[cur[1]] == True:
                continue
            if cur[1] == n:
                return cur[0]
            visited[cur[1]] = True
            for child in graph[cur[1]]:
                if visited[child[0]] == False:
                    if (cur[0] < t1 and cur[0] + child[1] <= t1) or (cur[0] >= t2):
                        heappush(heap, (cur[0] + child[1], child[0]))
                    else:
                        if t2 + child[1] >= cur[0] + child[2]:
                            heappush(heap, (cur[0] + child[2], child[0]))
                        else:
                            heappush(heap, (t2 + child[1], child[0]))
    temp = check(0)
    if temp <= t0:
        print(t0 - temp)
    else:
        print(-1)
    # l = 0
    # r = t0
    # # print(l, r)
    # while l + 1 < r:
    #     m = (l + r) // 2
    #     # print(m)
    #     if check(m):
    #         l = m
    #     else:
    #         r = m - 1
    # if check(r):
    #     print(r)
    # elif check(l):
    #     print(l)
    # else:
    #     print(-1)
    # print(check(3))
    # print(graph)

for t in range(int(input())):
    solve()