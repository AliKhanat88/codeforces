import sys
input = sys.stdin.readline
from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    dict = defaultdict(lambda:0)
    for num in arr:
        dict[num] = m + 1

    for j in range(m, 0, -1):
        ind, val = map(int, input().split())
        dict[arr[ind-1]] -= j
        arr[ind-1] = val
        dict[val] += j
        # print(dict)

    # print(dict)
    sumi = 0
    for key, val in dict.items():
        sumi = sumi + (val-1) * (val) // 2 + (m+1 - val) * val

    print(sumi)
for t in range(int(input())):
    solve()