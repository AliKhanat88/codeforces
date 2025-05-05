from pprint import pprint
from collections import defaultdict

def solve():
    n, q = map(int, input().split())
    s = list(input())
    print("TEST")
    pprint(s)
    p_arr = [[0 for i in range(n+1)] for i in range(26)]

    for i in range(n):
        for j in range(ord("a"), ord("z") + 1):
            if s[i] == chr(j):
                p_arr[j - 97][i+1] = p_arr[j-97][i] + 1
            else: 
                p_arr[j - 97][i+1] = p_arr[j-97][i]
    # pprint(p_arr)


    for i in range(q):
        l, r = map(int, input().split())
        dict = {}
        print(l, r)
        for j in range(ord("a"), ord("z") + 1):
            if p_arr[j-97][r] - p_arr[j-97][l-1] > 0:
                dict[chr(j)] = p_arr[j-97][r] - p_arr[j-97][l-1]
        temp = r - l + 1
        if len(dict) == 1:
            print(0)
        elif len(dict) > 2:
            print((temp * (temp+1) // 2) - 1)
        elif len(dict) == 2:
            if temp % 2 == 0:
                print((temp * (temp+1) // 2) - 1)
            elif temp % 2 == 1:
                temp_arr = list(dict.items())
                print(temp_arr)
                if temp_arr[0][1] <= temp_arr[1][1]:
                    if temp_arr[0][1] == 1:
                        if s[l + temp // 2] == temp_arr[0][0]:
                            print((temp * (temp+1) // 2) - 1- temp)
                        else:
                            print((temp * (temp+1) // 2) - 1)
                    else:
                        print((temp * (temp+1) // 2) - 1)
                else:
                    if temp_arr[1][1] == 1:
                        if s[l+temp//2] == temp_arr[1][0]:
                            print((temp * (temp+1) // 2) - 1 - temp)
                        else:
                            print((temp * (temp+1) // 2) - 1)
                    else:
                        print((temp * (temp+1) // 2) - 1)

for t in range(int(input())):
    solve()
