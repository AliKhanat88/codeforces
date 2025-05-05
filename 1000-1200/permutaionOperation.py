import sys
input = sys.stdin.readline
from collections import defaultdict

def print_moves(n, arr):
    diff = [0] * n
    diff[0] = (0, 1)
    for i in range(1, n):
        diff[i] = (max(0, arr[i-1] - arr[i]), i+1)
    diff = sorted(diff, key=lambda x:x[0], reverse=True)
    # print(diff)
    dict = defaultdict(lambda:0)
    k = 0
    for i in range(n, 0, -1):
        dict[i] = diff[k][1]
        k += 1
    for i in range(n):
        print(dict[i+1], end=" ")
    print()

for t in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    print_moves(n, arr)