import sys
input = sys.stdin.readline

def solve():
    n, w = map(int, input().split())
    parent = [-1, -1] + list(map(int, input().split()))
    sumi = n * w
    cur = 0
    for i in range(n-1):
        a, b = map(int, input().split())
        if parent[a] == a - 1:
            sumi -= (w - cur)
        sumi += (b * 2)
        sumi -= (b * (n - i - 1))
        cur += b
        print(sumi, end = " ")
    print()

for t in range(int(input())):
    solve()