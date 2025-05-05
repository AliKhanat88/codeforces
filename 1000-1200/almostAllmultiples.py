def solve():
    n, x = map(int, input().split())
    arr = list(range(1, n+1))
    if n % x != 0:
        print(-1)
        return
    arr[0] = x
    arr[n-1] = 1
    if x != n:
        arr[x-1] = n
        i = x * 2
        per = x
        while i <= n // 2:
            if n % i == 0:
                arr[per-1] = i
                arr[i-1] = n
                per = i
            i += per
    print(" ".join([str(x) for x in arr]))

for t in range(int(input())):
    solve()