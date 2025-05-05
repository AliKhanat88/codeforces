def solve():
    s = list(input())
    ans = 0
    for i in range(len(s) // 2):
        ans += (abs(int(s[i]) - int(s[len(s) - i - 1])))
    print(ans)

for t in range(int(input())):
    solve()