def solve():
    n, a, b = map(int, input().split())
    if a >= b:
        print(n * a)
        return
    diff = min(b - a, n)
    ans = ((b + b - diff + 1) * (diff)) // 2 + (n - diff) * a
    print(ans)




for t in range(int(input())):
    solve()