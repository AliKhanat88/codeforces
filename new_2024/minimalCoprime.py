def solve():
    l, r = map(int, input().split())
    ans = 0
    if l == 1:
        ans = 1
        l += 1
    if r > l:
        ans += (r - l)
    print(ans)

for t in range(int(input())):
    solve()