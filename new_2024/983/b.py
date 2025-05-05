def solve():
    n, k = map(int, input().split())
    if n == 1 and k == 1:
        print(1)
        print(1)
        return
    if k == n // 2 + 1:
        print(n)
        print(*[i for i in range(1, n+1)])
        return 
    if k == 1 or k == n:
        print(-1)
        return
    if (n - k) % 2 == 1:
        print(3)
        print(1, k, k+1)
    else:
        l = k - 1
        r = k + 1
        ans1 = []
        ans2 = []
        while l > 0 and r <= n:
            ans1.append(l)
            ans2.append(r)
            l -= 1
            r += 1
        ans1[-1] = 1
        print(len(ans1) + len(ans2) + 1)
        print(*ans1[::-1], k, *ans2)

        

for t in range(int(input())):
    solve()