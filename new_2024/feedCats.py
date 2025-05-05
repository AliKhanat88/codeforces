import sys
input = sys.stdin.readline
from heapq import heappop, heappush


def solve():
    n, m = map(int, input().split())
    arr = [0] * m
    for i in range(m):
        a, b = map(int, input().split())
        arr[i] = (a, b, i)
    
    
    discard = [False] * m
    dp = [0] * (n + 1)
    arr.sort()
    # print(arr)
    heap_f = []
    heap_s = []
    j = 0
    for i in range(1, n+1):
        while j < m:
            if arr[j][0] == i:
                heappush(heap_s, (arr[j][1], arr[j][2]))
                heappush(heap_f, (arr[j][0], arr[j][2]))
                j += 1
            else:
                break
        
        while len(heap_s) > 0:
            if heap_s[0][0] < i:
                discard[heap_s[0][1]] = True
                heappop(heap_s)
            else:
                break
        
        while len(heap_f) > 0:
            if discard[heap_f[0][1]]:
                heappop(heap_f)
            else:
                break
        if len(heap_s) == 0:
            dp[i] = dp[i-1]
        else:
            dp[i] = max(dp[i-1], len(heap_s) + dp[heap_f[0][0] - 1])
    #     print(heap_s)
    #     print(heap_f)
    # print(dp)
    print(dp[n])
        
for t in range(int(input())):
    solve()