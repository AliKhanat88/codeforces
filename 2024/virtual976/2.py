import sys
input = sys.stdin.readline
from math import isqrt
N = 10000001

arr = [True] * N
for i in range(2, isqrt(N)+1):
    for j in range(i+i, N, i):
        arr[j] = False

ans = [0] * (N)
per = 2
ans[5] = 2
for i in range(6, N):
    if arr[i] == True:
        if arr[i - 2] == True:
            per += 1
    ans[i] = per
# print(arr[29])
def solve(t):
    n = int(input())
    print(f"Case #{t+1}: {ans[n]}")
    
for t in range(int(input())):
    solve(t)