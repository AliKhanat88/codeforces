from collections import Counter
def solve():
    n, m = map(int, input().split())
    c = Counter(input())
    ans = 0
    for i in range(ord("A"), ord("G")+1):
        if c[chr(i)] < m:
            ans += m - c[chr(i)]
    print(ans)
for t in range(int(input())):
    solve()