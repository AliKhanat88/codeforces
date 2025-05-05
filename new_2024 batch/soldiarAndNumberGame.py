from math import sqrt
import sys
input = sys.stdin.readline
n = 5000001
a = [n] * 5000001

for i in range(2, int(sqrt(n))+1):
    if a[i] == n:
        for j in range(i+i, n, i):
            a[j] = min(i, a[j])

sum_prime = [0] * n

for i in range(2, n):
    if a[i] == n:
        sum_prime[i] = 1
    else:
        sum_prime[i] = sum_prime[i // a[i]] + 1

for i in range(1, n):
    sum_prime[i] = sum_prime[i-1] + sum_prime[i]
# print(a[443])

def solve():
    b, a= map(int, input().split())
    print(sum_prime[b] - sum_prime[a])

for t in range(int(input())):
    solve()
