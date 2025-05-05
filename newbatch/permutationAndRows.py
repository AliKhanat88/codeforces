import sys

input = sys.stdin.readline

from collections import defaultdict

from pprint import pprint

def solve():
    n, m = map(int, input().split())
    arr = [0] * n
    for i in range(n):
        arr[i] = list(map(int, input().split()))

    brr = [0] * n
    for i in range(n):
        brr[i] = list(map(int, input().split()))

    # index_sec = [0] * n

    # dict_a = defaultdict(lambda: -1)
    # for i in range(n):
    #     for j in range(m):
    #         dict_a[arr[i][j]] = i

    dict_b = defaultdict(lambda: -1)
    for i in range(n):
        for j in range(m):
            dict_b[brr[i][j]] = i

    crr = [0] * n

    for i in range(n):
        crr[i] = brr[dict_b[arr[i][0]]]

    arr_a = [[0 for i in range(n)] for i in range(m)]

    for i in range(n):
        for j in range(m):
            arr_a[j][i] = arr[i][j]

    arr_c = [[0 for i in range(n)] for i in range(m)]

    for i in range(n):
        for j in range(m):
            arr_c[j][i] = crr[i][j]
    # print("TEST")
    # pprint(arr)
    # print("BRR")
    # pprint(arr_a)
    # pprint(crr)
    # pprint(arr_c)

    arr_a.sort(key= lambda x: x[0])

    arr_c.sort(key=lambda x: x[0])


    for i in range(n):
        for j in range(m):
            if arr_a[j][i] != arr_c[j][i]:
                print("NO")
                return
    
    print("YES")

    


for t in range(int(input())):
    solve()