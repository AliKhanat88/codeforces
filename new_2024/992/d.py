import sys
input = sys.stdin.readline


def solve():
    n = int(input())
    adj = [[] for i in range(n+1)]
    for i in range(n - 1):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    visited = [False] * (n + 1)
    dfs = [(1, 0)]
    ans = [-1] * (n + 1)
    while dfs:
        cur = dfs.pop()

    
for t in range(int(input())):
    solve()