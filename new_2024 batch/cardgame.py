from collections import Counter
def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    c = Counter(arr)
    c2 = Counter(c.values())
    print(c2[2])

for t in range(int(input())):
    solve()