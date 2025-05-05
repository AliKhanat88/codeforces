from collections import defaultdict
import sys
imput = sys.stdin.readline

def solve():
    n,m = map(int, input().split())
    s = input()

    arr_sorted = [-1] * n
    arr_first = [-1] * n
    arr_second = [-1] * n

    arr_sorted[0] = 0
    arr_first[0] = 0
    arr_second[0] = 0
    per1 = 0
    per2 = 0
    per3 = 0
    if s[0] == "1":
        per2 += 1
    
    for i in range(1, n):
        if s[i] < s[i-1]:
            per1 += 1
        if s[i] == "0":
            per3 += 1
        arr_sorted[i] = per1
        arr_first[i] = per2
        arr_second[i] = per3
        if s[i] == "1":
            per2 += 1

    # print("TEST")
    # print(s)
    # print(arr_sorted)
    # print(arr_first)
    # print(arr_second)

    dict = {}
    isFirst = False
    for i in range(m):
        a, b = map(int, input().split())
        if arr_sorted[a-1] == arr_sorted[b-1]:
            isFirst = True
        else:
            dict[(arr_first[a-1], arr_second[b-1])] = True
    if isFirst:
        print(len(dict) + 1)
    else:
        print(len(dict))



            

for t in range(int(input())):
    solve()