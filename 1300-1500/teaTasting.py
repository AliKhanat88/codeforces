from collections import defaultdict
from bisect import bisect_right

def solve():
    n = int(input())
    a = [*map(int, input().split())]
    b = [*map(int, input().split())]

    dict = defaultdict(lambda:0)

    b_sum = [0] * n
    b_sum[0] = b[0]
    for i in range(1, n):
        b_sum[i] = b_sum[i-1] + b[i]
    # print(a)
    # print(b_sum)
    mult = [0] * (n+1)
    per = 0
    for i in range(n):
        if a[i] + per <= b_sum[i]:
            dict[i] += a[i]
            # mult[i] -= 1
        else:
            temp = bisect_right(b_sum, a[i] + per)
            mult[temp] += 1
            mult[i] -= 1
            dict[temp] += a[i] + per - b_sum[temp-1]
            
            # print(temp, i)
        per = b_sum[i]
    # print(mult)
    # print(dict)

    ans = [0] * n
    mul = mult[n]

    for i in range(n-1, -1, -1):
        ans[i] = f"{dict[i] + mul * b[i]}"
        mul += mult[i]
    print(" ".join(ans))


for t in range(int(input())):
    solve()