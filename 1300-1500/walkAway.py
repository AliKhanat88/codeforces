from math import ceil
from collections import Counter

def solve():
    c = Counter()
    n, m, d = map(int, input().split())
    arr = [*map(int, input().split())]
    if arr[0] != 1:
        arr = [1] + arr
    else:
        c[0] += 1
    maxi = 0
    org_ans = 1
    # print(arr)
    for i in range(1, len(arr) -1):
        temp = ceil((arr[i] - arr[i-1]) / d)
        new_maxi = temp + ceil((arr[i+1] - arr[i]) / d) - ceil((arr[i+1] - arr[i-1]) / d)
        maxi = max(maxi, new_maxi)
        c[new_maxi] += 1
        org_ans += temp
        # print(temp, org_ans, maxi)

    if arr[-1] != n:
        temp = ceil((arr[-1] - arr[-2]) / d)
        new_maxi = temp + (n - arr[-1]) // d - (n - arr[-2]) // d
        maxi = max(maxi, new_maxi)
        c[new_maxi] += 1
        org_ans += temp + (n - arr[-1]) // d
        # print(temp, org_ans, maxi)
    else:
        temp = ceil((arr[-1] - arr[-2]) / d)
        new_maxi = temp - (arr[-1] - arr[-2]) // d
        maxi = max(maxi, new_maxi)
        c[new_maxi] += 1
        org_ans += temp
        # print(temp, org_ans, maxi)
    # print(c)
    print(org_ans - maxi, c[maxi])
for t in range(int(input())):
    solve()