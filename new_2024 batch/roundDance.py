from collections import defaultdict

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    graph = defaultdict(lambda: [])
    for i in range(1, n+1):
        if arr[i-1] not in graph[i]:
            graph[i].append(arr[i-1])
        if i not in graph[arr[i-1]]:
            graph[arr[i-1]].append(i)

    # print(graph)
    # 123
    visited = [0] * (n+1)
    cycles = 0
    nonCycles = 0
    for i in range(1, n+1):
        if visited[i] == 0:
            cycleFound = False
            queue = [(i, -1)]
            while len(queue) != 0:
                cur = queue.pop()
                if visited[cur[0]] == -1:
                    cycleFound = True
                    break
                visited[cur[0]] = -1
                for num in graph[cur[0]]:
                    if num != cur[1]:
                        queue.append((num, cur[0]))
            if cycleFound == True:
                cycles += 1
            else:
                nonCycles += 1
        # print(visited)
    if nonCycles > 0:
        print(cycles+1, cycles+nonCycles)
    else:
        print(cycles, cycles+nonCycles)

for t in range(int(input())):
    solve()