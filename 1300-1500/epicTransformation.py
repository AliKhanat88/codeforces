from collections import Counter
from heapq import *

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    c_arr = Counter(arr).values()

    c_arr = list(map(lambda x: -x, c_arr))
    heapify(c_arr)
    # print(c_arr)
    while len(c_arr) > 1:
        a = heappop(c_arr)
        b = heappop(c_arr)
        if a + 1 != 0:
            heappush( c_arr, a+1)
        if b + 1 != 0:
            heappush( c_arr, b+1)
    
    print(-sum(c_arr))





for t in range(int(input())):
    solve()
