from collections import defaultdict
import sys
input = sys.stdin.readline

def solve():
    input()
    n, k = map(int, input().split())
    friends = list(map(int, input().split()))
    graph = defaultdict(lambda: [])
    time = defaultdict(lambda:999999999999999)

    frientExist = [-1] * (n+1)
    for friend in friends:
        frientExist[friend] = 1
    for i in range(n-1):
        a,b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for friend in friends:
        queue = [(friend, 0)]
        while len(queue) != 0:
            cur = queue.pop(0)
            if time[cur[0]] > cur[1]:
                time[cur[0]] = cur[1]
            else:
                continue
            for num in graph[cur[0]]:
                if num != cur[0] and frientExist[num] == -1:
                    queue.append((num, cur[1] + 1))
    

    queue = [(1, 0)]
    while len(queue) != 0:
        cur = queue.pop(0)
        if time[cur[0]] <= cur[1]:
            continue
        if len(graph[cur[0]]) == 1 and cur[0] != 1:
            print("YES")
            return
        for num in graph[cur[0]]:
            if num != cur[0]:
                queue.append((num, cur[1] + 1))
    print("NO")
    # print(time)
for t in range(int(input())):
    solve()