def solve():
    n, k1, k2 = map(int, input().split())
    s = list(input())
    ans = int(s[0]) * k1
    per = k1
    for i in range(1, n):
        temp = min(k2 - int(s[i-1]) * per, k1 * int(s[i]))
        ans += min(k2 - int(s[i-1]) * per, k1 * int(s[i]))
        per = temp
        
    print(ans)

for t in range(int(input())):
    solve()