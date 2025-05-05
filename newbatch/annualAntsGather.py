from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    visited = [False] * (n+1)
    children = [0] * (n+1)
    tree = [[] for i in range(n+1)]
    for i in range(n-1):
        a, b = map(int, input().split())
        children[a] += 1
        children[b] += 1
        tree[a].append(b)
        tree[b].append(a)
    heapi = []
    for i in range(1, n+1):
        if children[i] == 1:
            heapi.append((1, i))
    ans = [1] * (n+1)
    while len(heapi) != 0:
        top = heappop(heapi)
        visited[top[1]] = True
        for par in tree[top[1]]:
            if visited[par] == False:
                if ans[par] < ans[top[1]]:
                    print("NO")
                    return
                children[par] -= 1
                ans[par] += ans[top[1]]
                if children[par] == 1:
                    heappush(heapi, (ans[par], par))
                break
    # print(heapi)
    # print(ans)
    print("YES")
solve()