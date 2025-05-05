import sys
input = sys.stdin.readline
from math import isqrt

def solve():
    w, b = map(int, input().split())
    n = isqrt(2 * (w + b))
    if (n * (n + 1)) // 2 <= w + b:
        print(n)
    else:
        print(n - 1)


for t in range(int(input())):
    solve()