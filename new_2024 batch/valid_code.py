from ratingSystem import solve
from itertools import combinations
from random import randint

def valid(n, arr):

    maxi = 0
    max_k = 0
    for i in range(230 * n + 1):
        sumi = 0
        if i == 0:
            active = True
        else:
            active = False
        for j in range(n):
            if active:
                sumi = max(sumi + arr[j], i)
            else:
                sumi += arr[j]
            if sumi >= i:
                active = True
        if sumi > maxi:
            maxi = sumi
            max_k = i
    return maxi, max_k
    
def temp_valid(n, arr, ans):
    if ans == 0:
        active = True
    else:
        active = False
    sumi = 0
    for j in range(n):
        if active:
            sumi = max(sumi + arr[j], ans)
        else:
            sumi += arr[j]
        if sumi >= ans:
            active = True
    return sumi

# print(temp_valid(7, [3 ,-10 ,20 ,-7 ,5 ,-4, -5], ))


def stress_testing(n, c):
    for i in range(100000000):
        arr = [randint(-230, 230) for i in range(n)]
        # temp = combinations(arr, c)
        # for comb in temp:
        sol1 , temp_sol1 = valid(n, arr)
        temp_sol2 = solve(n, arr)
        sol2 = temp_valid(n, arr, temp_sol2)

        if sol2 != sol1:

            print("n", c, "arr", arr, " not valid", "sol1", sol1, "sol2", sol2,  "temp_sol2", temp_sol2,  "temp_sol1", temp_sol1)
            break


stress_testing(20, 7)