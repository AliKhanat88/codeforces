from collections import Counter
from math import isqrt

def return_index(x, dimentions):
    index = [0] * len(dimentions)
    for i in range(len(dimentions)-1, -1,-1):
        index[i] = x % dimentions[i][1]
        x = x // dimentions[i][1]
    return index

def get_single(index, dimentions):
    x = 0
    pro = 1
    for i in range(len(index)-1, -1, -1):
        x = x + (index[i]) * pro
        pro = pro * dimentions[i][1]
    # x += index[-1]
    return x

def get_primes(x):
    c = Counter()
    i = 2
    temp = isqrt(x)
    while i <= temp:
        while x % i == 0:
            x = x // i
            c[i] += 1
        i += 1
    if x != 1:
        c[x] += 1
    return c

def get_index_sum(x, temp_c, dimentions):
    index = return_index(x, dimentions)
    i = 0
    for key, val in dimentions:
        index[i] = index[i] + temp_c[key]
        if index[i] >= dimentions[i][1]:
            return -1, False
        i += 1
    return get_single(index, dimentions), True

def solve():
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    c = get_primes(x)
    # print(c)
    dimentions = c.items()
    dimentions = [(x[0], x[1]+1) for x in dimentions]
    dimention_keys = [num[0] for num in dimentions]
    # print(dimentions)
    length = 1
    for num in dimentions:
        length = length * (num[1])
    dp = [False for i in range(length)]
    dp[0] = True
    # print(dp)
    # temp = return_index(23, dimentions)
    # print(temp)
    # print(get_single(temp, dimentions))
    ans = 1
    i = 0
    while i < n:
        if arr[i] != 1:
            temp_c = get_primes(arr[i])
            can = True
            for key, val in temp_c.items():
                if key not in dimention_keys:
                    can = False
                    break
            if can == True:
                for j in range(len(dp)-1, -1, -1):
                    if dp[j] == True:
                        temp_i, can_oper = get_index_sum(j,temp_c, dimentions)
                        if can_oper and temp_i < len(dp):
                            dp[temp_i] = True
        # print(dp)
        if dp[-1] == True:
            ans += 1
            dp = [False] * length
            dp[0] = True
            i -= 1
        i += 1
    print(ans)
for t in range(int(input())):
    solve()