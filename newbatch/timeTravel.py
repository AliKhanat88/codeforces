import sys 
input = sys.stdin.readline
from collections import defaultdict
from heapq import heappop, heappush
from bisect import bisect_left

n, t = map(int, input().split())
graphs = [defaultdict(lambda:[]) for  i in range(t+1)]
occur = [set() for i in range(n+1)]
for i in range(t):
    for j in range(int(input())):
        a, b = map(int, input().split())
        graphs[i+1][a].append(b)
        graphs[i+1][b].append(a)
        occur[a].add(i+1)
        occur[b].add(i+1)


k = int(input())
arr = list(map(int, input().split()))
occur_t = [[] for i in range(t+1)]
for i in range(k):
    occur_t[arr[i]].append(i+1)


# print(occur)
# print(graphs)
# print(arr)
# print(occur_t)

heap = [(0, 1)]
done = [-1] * (n+1)
while len(heap) != 0:
    cur = heappop(heap)
    if done[cur[1]] == -1:
        done[cur[1]] = 0
        if cur[1] == n:
            print(cur[0])
            exit()
        for time in occur[cur[1]]:
            temp = bisect_left(occur_t[time], cur[0]+1)
            if temp >= len(occur_t[time]):
                continue
            for num in graphs[time][cur[1]]:
                if done[num] == -1:
                    heappush(heap, (occur_t[time][temp], num))

print(-1)