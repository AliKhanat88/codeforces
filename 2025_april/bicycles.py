import sys
input = sys.stdin.readline
from collections import defaultdict
from heapq import heappop, heappush

def solve():
    n, m = map(int, input().split())
    adj = defaultdict(lambda: [])
    inf = 1 << 40
    distances = defaultdict(lambda: defaultdict(lambda: inf))
    for i in range(m):
        a, b, w = map(int, input().split())
        adj[a].append((b,w))
        adj[b].append((a, w))
    s = list(map(int, input().split()))
    heapi = [(0, 1, s[0])]
    distances[0][s[0]] = 0
    while len(heapi) > 0:
        dist, node, cur_s = heappop(heapi)
        for child in adj[node]:
            temp_s = min(cur_s, s[child[0]-1])
            new_dist = dist + child[1] * cur_s
            if distances[child[0]][temp_s] > new_dist:
                distances[child[0]][temp_s] = new_dist
                heappush(heapi, (new_dist, child[0], temp_s))
    print(min(distances[n].values()))
    
for t in range(int(input())):
    solve()