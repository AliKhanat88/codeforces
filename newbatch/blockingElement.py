inf = 999999999999999999
from heapq import heappop, heappush
import sys
input = sys.stdin.readline
def check(arr, sumi_arr, mid):
    dp = [inf] * len(arr)
    heap = [(0, -1)]
    for i in range(len(arr)):
        while len(heap) != 0:
            if sumi_arr[i] - sumi_arr[heap[0][1] + 1] > mid:
                heappop(heap)
            else:
                break
        if len(heap) == 0:
            return False
        dp[i] = heap[0][0] + arr[i]
        heappush(heap, (dp[i], i))
    # print(dp, mid)
    sumi = 0
    i = len(dp)-1
    while i > -1 and sumi <= mid:
        if dp[i] <= mid:
            return True
        sumi += arr[i]
        i -= 1
    return False


def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    # print("TEST")
    # print(arr)
    sumi_arr = [0] * (n+1)
    for i in range(1, n+1):
        sumi_arr[i] = sumi_arr[i-1] + arr[i-1]
    
    # print(sumi_arr)

    lower = max(arr)
    higher = sum(arr)
    while lower +1 < higher:
        mid = (lower + higher) // 2
        temp = check(arr, sumi_arr, mid)
        if temp == True:
            higher = mid
        else:
            lower = mid + 1
    if check(arr, sumi_arr, lower):
        print(lower)
    else:
        print(higher)
    # print(lower, higher)
for t in range(int(input())):
    solve()