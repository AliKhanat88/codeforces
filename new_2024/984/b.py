from collections import defaultdict

def solve():
    n, k = map(int, input().split())
    dict = defaultdict(lambda: 0)
    for i in range(k):
        a, b = map(int, input().split())
        dict[a] += b

    vals = list(dict.values())
    vals.sort(reverse=True)
    i = 1
    j = 0
    ans = 0
    while i <= n and j < len(vals):
        ans += vals[j]
        j += 1
        i += 1
    print(ans)

for t in range(int(input())):
    solve()