from collections import deque


def solve():
    n = int(input())
    adj = [[] for i in range(n+1)]

    for i in range(n-1):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    first = 1
    last = 2 * n - 1
    queue = deque()
    queue.append((1, 0, 0))
    ans = [0] * (n+1)
    visited = [False] * (n + 1)
    while queue:
        cur = queue.popleft()
        if not visited[cur[0]]:
            visited[cur[0]] = True
            if cur[2] % 2 == 0:
                if abs(first - ans[cur[1]]) == 2:
                    ans[cur[0]] = ans[cur[1]] + 1
                else:
                    ans[cur[0]] = first
                    first += 2
            else:
                if abs(last - ans[cur[1]]) == 2:
                    ans[cur[0]] = ans[cur[1]] + 1
                else:
                    ans[cur[0]] = last
                    last -= 2
            for child in adj[cur[0]]:
                queue.append((child, cur[0], cur[2] + 1))
    print(*ans[1:])
for t in range(int(input())):
    solve()