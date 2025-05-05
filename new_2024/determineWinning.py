import sys
input = sys.stdin.readline
from collections import defaultdict

inf = 99999999999999999999
def solve():
    n, m = map(int, input().split())
    edges = defaultdict(lambda: [])
    max_edge = defaultdict(lambda: None)

    for i in range(1, n):
        edges[i].append(i+1)
        max_edge[i] = i+1
    
    for i in range(m):
        a, b = map(int, input().split())
        edges[a].append(b)
        max_edge[a] = max(max_edge[a], b)
    
    mini_dp = [inf] * (n + 1)
    mini_dp[1] = 0
    for i in range(1, n):
        for edge in edges[i]:
            mini_dp[edge] = min(mini_dp[edge], mini_dp[i] + 1)
    
    # print(mini_dp)
    maxi = 0
    ans = []
    for i in range(1, n):
        # print(maxi, i)
        if maxi <= 0:
            ans.append("1")
        else:
            ans.append("0")
        if i >= n-1:
            break
        maxi = max(maxi - 1, max_edge[i] - i - mini_dp[i] - 2)
    print("".join(ans))



for t in range(int(input())):
    solve()