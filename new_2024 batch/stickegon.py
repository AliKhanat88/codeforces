from collections import Counter

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    c = Counter(arr)
    ans = 0
    for key, val in c.items():
        ans += val // 3
    print(ans)

for t in range(int(input())):
    solve()