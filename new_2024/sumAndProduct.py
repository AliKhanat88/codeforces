import sys
input = sys.stdin.readline
from collections import Counter
from random import randint
from math import isqrt


def solve():
    c = Counter()
    randi = randint(1, 2 ** 64)

    def get(x):
        return c[x ^ randi]
    def update(x, val):
        c[x ^ randi] += val
    
    n = int(input())
    arr = list(map(int, input().split()))
        
    for i in range(n):
        update(arr[i], 1)
    q = int(input())
    ans = []
    for i in range(q):
        s, p = map(int, input().split())
        inner = s ** 2 - 4 * p
        if inner >= 0 and isqrt(inner) ** 2 == inner:
            # print(s, p, "query")
            # print(inner, "inner")
            inner = isqrt(inner)
            first = s + inner
            second = s - inner
            # print(first / 2, second / 2, "roots")
            sumi = 0
            if first % 2 == 0:
                first = first // 2
                if first == s - first:
                    sumi += (get(first) * (get(first) - 1)) // 2
                else:
                    sumi += (get(first) * get(s - first))
            # print(first, "first")
            if second % 2 == 0 and second // 2 != first and second // 2 != (s - first):
                if second == s - second:
                    sumi += (get(second) * (get(second) - 1)) // 2
                else:
                    sumi += (get(second) * get(s - second))
            ans.append(sumi)
        else:
            ans.append(0)
    print(*ans)




for t in range(int(input())):
    solve()