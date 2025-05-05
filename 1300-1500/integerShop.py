import sys
input = sys.stdin.readline
from heapq import heapify, heappop, heappush

def solve():
    n = int(input())
    temp = [*map(int, input().split())]
    arr_mini = [(temp[0], temp[2], 0)]
    arr_maxi = [(-temp[1], temp[2], 0)]
    mini = temp[2]
    print(mini)
    per_mini = temp[0]
    per_maxi = temp[1]
    for i in range(1, n):
        temp = [*map(int, input().split())]
        heappush(arr_mini, (temp[0], temp[2], i))
        heappush(arr_maxi, (-temp[1], temp[2], i))
        if temp[0] < per_mini and temp[1] > per_maxi:
            mini = temp[2]
            per_mini = temp[0]
            per_maxi = temp[1]
            print(mini)
            continue
        if temp[0] > per_mini and temp[1] < per_maxi:
            print(mini)
            continue
        if per_mini <= arr_mini[0][0] and per_maxi >= abs(arr_maxi[0][0]):
            pass
        else:
            mini = 999999999999999999999
        if temp[0] <= arr_mini[0][0] and temp[1] >= abs(arr_maxi[0][0]):
            mini = min(mini, temp[2])
        mini = min(mini, arr_mini[0][1] + arr_maxi[0][1])
        per_mini = arr_mini[0][0]
        per_maxi = abs(arr_maxi[0][0])
        print(mini)



for t in range(int(input())):
    solve()