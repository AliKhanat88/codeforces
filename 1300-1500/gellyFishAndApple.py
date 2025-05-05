from collections import defaultdict
from math import log2

def solve():
    dict = defaultdict(lambda:0)
    n, m = map(int, input().split())
    ans = 0
    k = n
    while k < m:
        ans += k
        k = k * 2
    k = k % m
    if k == 0:
        print(ans)
        return 
    temp_m = m
    while temp_m % 2 == 0:
        temp_m = temp_m // 2
    if k % temp_m != 0:
        print(-1)
        return
    while k % m != 0:
        if k > m:
            k = k % m
        ans += k
        k *= 2
    print(ans)


for t in range(int(input())):
    solve()