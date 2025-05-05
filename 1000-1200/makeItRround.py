def solve():
    n, m = map(int, input().split())
    tens = 0
    temp = n
    while temp != 0:
        if (temp / 10) % 1 == 0:
            temp = int(temp / 10)
            tens += 1
        else:
            break
    tens += 1
    i = 2
    k = 1
    ans = n
    while i <= m:
        ans = n * (i//k)
        if (ans) % (10 ** tens) == 0:
            n = ans
            k = i
            tens += 1
        i += k
    print(ans)

for t in range(int(input())):
    solve()