from math import ceil
from decimal import Decimal

def solve():
    n, k = map(int, input().split())

    if k > n:
        print("NO")
        return
    elif k == n:
        print("YES")
        print(1)
        print(1)
    elif (k > n // 2 and n % 2 == 0) or (k > n // 2 + 1 and n % 2 == 1):
        print("NO")
    else:
        print("YES")
        print(2)
        print(n - k + 1, 1) 


for t in range(int(input())):
    solve()