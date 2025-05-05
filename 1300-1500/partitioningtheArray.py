# from bisect import bisect_right
from math import gcd

# small = [-1] * 200001
# for i in range(4, 448):
#     if i % 2 != 0 and i % 3 != 0:
#         for j in range(i, 200001, i):
#             if j % 2 != 0 and j % 3 != 0 and small[j] == -1:
#                 small[j] = i
# print(small)
def give_small(x):
    # if x % 2 == 0:
    #     return 2
    # elif x % 3 == 0:
    #     return 3
    # elif small[x] != -1:
    #     return small[x]
    # else:
    #     return x
    for i in range(2, int(x ** .5) +1):
        if x % i == 0:
            return i
    return x
    
# print(give_small(199999))
def key_func(x, n, arr):
    k = n // x
    temp1 = 0
    # print(x, n, arr)
    for i in range(k-1):
        temp2 = (i+1)*x
        for j in range(x):
            temp1 = gcd(temp1, abs(arr[j] - arr[j+temp2]))

    if temp1 != 1:
        return 1
    return 0

def solve():
    n = int(input())
    arr = [*map(int, input().split())]
    ans = 1
    for i in range(1, n//2 + 1):
        if n % i == 0:
            ans += key_func(i, n, arr)
    print(ans)
    


for t in range(int(input())):
    solve()