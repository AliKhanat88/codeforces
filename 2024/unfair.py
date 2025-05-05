def solve():
    a, b, c, d = map(int, input().split())
    ans = 0
    if a % 2 != b % 2:
        if (a + c) % 2 != 0 and a > 0:
            a -= 1
        elif (b + c) % 2 != 0 and b > 0:
            b -= 1
        elif b == 0:
            a -= 1
        else:
            b -= 1
    # print("TEST")
    # print(a,b,c,d)
    if a % 2 == 0:
        ans += (c // 2)
    else:
        ans += ((c+1) // 2)
    ans += (a // 2)
    ans += (b // 2)
    ans += (d // 2)
    print(ans)
for t in range(int(input())):
    solve()