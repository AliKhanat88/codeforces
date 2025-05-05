from heapq import heappop, heappush, heapify
import sys
input=sys.stdin.readline


def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    # n = 200000
    # arr = [i for i in range(1, n+1)]

    maxi_arr = [-1] * n
    maxi_arr[0] = (arr[0], 0)
    maxi_index = 0
    maxi_val = arr[0]
    for i in range(1, n):
        if arr[i] >= maxi_val:
            maxi_val = arr[i]
            maxi_index = i
        maxi_arr[i] = (maxi_val, maxi_index)
    
    # print(arr)
    # print(maxi_arr)
    maxi = [0] * n
    arr = [(arr[i], i) for i in range(n)]
    arr.sort(key = lambda x: (-x[0], -x[1]))
    maxi[arr[0][1]] = arr[0][0]
    heap = [(-arr[i][1], arr[i][0]) for i in range(n)]
    heapify(heap)
    

    for i in range(1, n):
        while len(heap) > 0 and heap[0][1] >= arr[i][0]:
            heappop(heap)
        temp = arr[i][1]
        if len(heap) > 0:
            temp = max(arr[i][1], -heap[0][0])
        # print(maxi_arr[temp], i, arr[i])
        ans = maxi_arr[temp]
        if ans[0] == arr[i][0]:
            maxi[arr[i][1]] = arr[i][0]
        else:
            maxi[arr[i][1]] = maxi[ans[1]]
    print(*maxi)
        

for t in range(int(input())):
    solve()