from collections import Counter

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    c = Counter(arr)

    print(n - max(c.values()))


for t in range(int(input())):
    solve()
               