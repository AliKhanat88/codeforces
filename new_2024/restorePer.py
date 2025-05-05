import sys
input = sys.stdin.readline
from heapq import heappop, heappush

def solve(n, arr):

    index = [-1] * (n+1) 

    for i in range(n//2):
        if index[arr[i]] != -1:
            print(-1)
            return -1
        index[arr[i]] = i
    
    heap = []
    ans = [0] * (n + 1)
    for i in range(n, 0 , -1):
        if index[i] == -1:
            if len(heap) == 0:
                print(-1)
                return -1
            temp = heappop(heap)
            ans[temp[1]] = i
        else:
            heappush(heap, (-index[i], i))
    
    for i in range(n // 2):
        print(ans[arr[i]], arr[i], end=" ")

    print()

    





from itertools import permutations


def brute(n, arr):
    combs = permutations([i for i in range(1, n+1)])
    
    mini = [99999999999999999999999999999]
    for comb in combs:
        comb = list(comb)
        can = True
        for i in range(1, n, 2):
            if max(comb[i], comb[i-1]) != arr[i // 2]:
                can = False
                break
        # print(comb)
        if can and comb < mini:
            mini  = comb
    if mini == [99999999999999999999999999999]:
        return -1
    return mini

import random

def checker():
    n = 6
    for i in range(100):
        arr = random.sample([i for i in range(1, n+1)], n//2)
        if brute(n, arr) != solve(n, arr):
            print("Found")
            print(arr)
            print(brute(n, arr), "brute")
            print(solve(n, arr), "solve")
            exit()

# checker()


for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    solve(n, arr)