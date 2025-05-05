# import sys

# input = sys.stdin.readline

# def solve():
#     n = int(input())

#     arr = [0, *list(map(int, input().split()))]

#     for i in range(1, n+1):
#         arr[i] += arr[i-1]
    
#     q = int(input())
#     for i in range(q):
#         l, u = map(int, input().split())
#         upper = n
#         lower = l
#         while lower < upper - 1:
#             mid = lower + (upper - lower) // 2
#             if arr[mid] - arr[l-1] <= u + 1 and arr[mid] - arr[l-1] >= u:
#                 upper = mid
#             elif arr[mid] - arr[l-1] > u + 1:
#                 upper = mid - 1
#             else:
#                 lower = mid
#         if arr[upper] - arr[l-1] >= u+1:
#             print(lower, end=" ")
#         else:
#             print(upper, end=" ")
#     print()

# for t in range(int(input())):
#     solve()

from math import ceil

def k(a, b, c):
    ans = a
    if b % 3 > 0 and (b % 3) + c < 3:
        return -1
    ans += ceil((b + c) / 3)
    return ans


t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    ans = k(a, b, c)
    print(ans)