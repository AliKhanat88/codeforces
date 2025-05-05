from collections import defaultdict
import sys
input = sys.stdin.readline

def print_permute(n, arr):
    dict = defaultdict(lambda:[0, 0, False])
    for i in range(n):
        dict[arr[i]][0] += 1
        if dict[arr[i]][0] > 2:
            print("NO")
            return
    # print(dict)
    missing_arr = []
    sort_arr = sorted(set(arr))
    k = len(sort_arr)
    per = 1
    i = 0
    while i < k:
        if sort_arr[i] != per:
            while sort_arr[i] != per and per < n:
                missing_arr.append(per)
                per += 1
        per += 1
        if dict[sort_arr[i]][0] == 2:
            if len(missing_arr) == 0:
                print("NO")
                return
            else:
                dict[sort_arr[i]][1] = missing_arr.pop(0)
        i += 1
    p = ""
    q = ""
    for i in range(n):
        if dict[arr[i]][0] == 2:
            if dict[arr[i]][2] == False:
                p += f"{arr[i]} "
                q += f"{dict[arr[i]][1]} "
                dict[arr[i]][2] = True
            else:
                p += f"{dict[arr[i]][1]} "
                q += f"{arr[i]} "
        else:
            p += f"{arr[i]} "
            q += f"{arr[i]} "
    print("YES")
    print(p)
    print(q)



for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print_permute(n, arr)