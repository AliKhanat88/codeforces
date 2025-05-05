import sys
input = sys.stdin.readline
from decimal import Decimal

def solve(t):
    n = int(input())
    low = float("-inf")
    high = float("inf")
    # print("TEST")
    arr = [0]* n
    for i in range(n):
        a, b = map(int, input().split())
        arr[i] = (a, b)
    for i in range(n):
        a, b = arr[i]
        if a == 0:
            templ = float("inf")
        else:
            templ = Decimal((i+1)) / Decimal(a)
        tempr = Decimal((i+1)) / Decimal(b)
        if templ < low:
            print(f"Case #{t+1}: {-1}")
            return
        if tempr > high:
            print(f"Case #{t+1}: {-1}")
            return
        # print(low, high, templ, tempr)
        low = max(low, tempr)
        high = min(high, templ)
    print(f"Case #{t+1}: {low}")
for t in range(int(input())):
    solve(t)