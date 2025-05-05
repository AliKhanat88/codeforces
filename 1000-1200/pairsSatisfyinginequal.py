import sys
input = sys.stdin.readline
from collections import defaultdict

def print_count(n, arr):
    diction = defaultdict(lambda:-1)
    for i in range(n):
        if i+1 > arr[i]:
            diction[i+1] = arr[i]
    counts = [0] * n
    sort_arr = sorted(diction.items(), key= lambda x : x[1])
    per  = len(sort_arr) -1 
    per_count = 0
    i = n-1
    while i >= 0:
        if diction[i+1] == -1:
            counts[i] = 0
            i -= 1
        else:
            if per >= 0 and i+1 < sort_arr[per][1]:
                per_count += 1
                per -= 1
            else:
                counts[i] = per_count
                i = i - 1
    print(sum(counts))
for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print_count(n, arr)