from collections import defaultdict
def can_make(n, arr):
    # finding mex
    sort_arr = sorted(set(arr))
    i = 0
    dict = defaultdict(lambda:0)
    while i < len(sort_arr):
        if sort_arr[i] != i:
            mex = i
            break
        i += 1
    if i == len(sort_arr):
        mex = i

    can_add = False
    # left side of mex+1 
    i = 0
    while i < n:
        if arr[i] > mex + 1:
            can_add = True
        elif arr[i] == mex+1:
            can_add = True
            break
        else:
            dict[arr[i]] += 1
        i += 1
    
    # right side of mex + 1
    j = n-1
    while j > i:
        if arr[j] > mex + 1:
            can_add = True
        elif arr[j] == mex+1:
            can_add = True
            break
        else:
            dict[arr[j]] += 1
        j -= 1

    # in between
    for k in range(i+1, j):
        if arr[k] < mex+1 and dict[arr[k]] <= 0:
            print("NO")
            return

    for key, value in dict.items():
        if value > 1:
            can_add = True
            break
    if can_add == True:
        print("YES")
    else:
        print("NO")


for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    can_make(n, arr)