def solve():
    n = int(input())
    ans = 0
    if n % 2 == 1:
        ans += (n + 1) // 2
        n -= 1
    temp = (n) // 2
    ans += ((temp * (temp + 1) // 2) * 2)
    print(ans)

for t in range(int(input())):
    solve()