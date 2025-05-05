import sys
input = sys.stdin.readline
from heapq import heappop, heappush

def solve():
    # print("TEST")
    n, m, k, d = map(int, input().split())

    mini_arr = [0] * n
    for i in range(n):
        arr = list(map(int, input().split()))
        heapi = []
        # for j in range(d):
        #     # print(j)
        #     arr[j] += 1
        arr[0] = 1
        heappush(heapi, (1, 0))
        for j in range(1, m):
            temp = heappop(heapi)
            while temp[1] < j - d - 1:
                temp = heappop(heapi)
            arr[j] = arr[j] + temp[0] + 1
            heappush(heapi, (arr[j], j))
            heappush(heapi, temp)
        # print(arr, d)
        mini_arr[i] = arr[-1]
    mini = 9999999999999999
    for i in range(n-k+1):
        sumi = 0
        for j in range(i, i+k):
            sumi += mini_arr[j]
        mini = min(mini, sumi)
    print(mini)
for t in range(int(input())):
    solve()