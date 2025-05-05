def solve():
    n = int(input())
    w = 0
    h = 0
    for i in range(n):
        a, b = map(int, input().split())
        w = max(a, w)
        h = max(b, h)
    print(w * 2 + h * 2)
    # arr = list(map(int, input().split()))

for t in range(int(input())):
    solve()