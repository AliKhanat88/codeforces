import sys
input = sys.stdin.readline


def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    prefix = [[0 for i in range(n+1)] for i in range(31)]
    for i in range(n):
        for b in range(31):
            if arr[i] & (1 << b):
                prefix[b][i+1] = prefix[b][i] + 1
            else:
                prefix[b][i+1] = prefix[b][i]
    
    def check(l, r):
        sumi = 0
        for b in range(31):
            if prefix[b][r] - prefix[b][l - 1] >= r - l + 1:
                sumi += (1 << b)
        return sumi
    q = int(input())
    for i in range(q):
        l1, k = map(int, input().split())
        l = l1
        r = n
        while l + 1 < r:
            m = (l + r) // 2
            if check(l1, m) >= k:
                l = m
            else:
                r = m - 1
        if check(l1, r) >= k:
            print(r, end=" ")
        elif check(l1 ,l) >= k:
            print(l, end=" ")
        else:
            print(-1, end=" ")
    print()
for t in range(int(input())):
    solve()