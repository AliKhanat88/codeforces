from math import isqrt
from collections import defaultdict
import sys
input = sys.stdin.readline

def solve():
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    qrt = isqrt(n)
    queries = [0] * q
    for  i in range(q):
        a,b = map(int, input().split())
        queries[i] = (a-1, b-1, i)

    
    print("\n".join(ans))
    # return ans


if __name__ == "__main__":

    for t in range(int(input())):
        solve()