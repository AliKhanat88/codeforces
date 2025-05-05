from collections import Counter
def solve():
    n = int(input())
    graph = [[] for i in range(n+1)]
    for i in range(n-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    distance = [0] * (n + 1)
    stack = [(1, 0)]
    visited = [False] * (n + 1)
    while len(stack) != 0:
        cur = stack.pop()
        if not visited[cur[0]]:
            distance[cur[0]] = cur[1]
            visited[cur[0]] = True
            for child in graph[cur[0]]:
                stack.append((child, cur[1] + 1))
    # print(distance)
    maxi_1 = distance.index(max(distance))
    distance = [0] * (n + 1)
    stack = [(maxi_1, 0)]
    visited = [False] * (n + 1)
    while len(stack) != 0:
        cur = stack.pop()
        if not visited[cur[0]]:
            distance[cur[0]] = cur[1]
            visited[cur[0]] = True
            for child in graph[cur[0]]:
                stack.append((child, cur[1] + 1))
    maxi_2 = distance.index(max(distance))
    stack = [(maxi_2, 0)]
    visited = [False] * (n + 1)
    while len(stack) != 0:
        cur = stack.pop()
        if not visited[cur[0]]:
            distance[cur[0]] = max(distance[cur[0]], cur[1])
            visited[cur[0]] = True
            for child in graph[cur[0]]:
                stack.append((child, cur[1] + 1))
    # print(maxi_1, maxi_2)
    # print(distance)
    ans = 0
    c = Counter(distance)
    # print(c)
    for i in range(1, n+1):
        ans += c[i-1]
        print(min(n, ans), end = " ")
    print()

solve()