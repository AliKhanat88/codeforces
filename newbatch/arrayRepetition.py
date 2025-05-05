import sys
input = sys.stdin.readline
MAX = 10 ** 18 + 1
from bisect import bisect_left

def solve():
    
    n, q = map(int, input().split())
    arr = [0] * (n + 1)
    map_arr = []
    find_per = [-1] * (n+1)
    per = None
    for i in range(1, n+1):
        a, b = map(int, input().split())
        if arr[i-1] >= MAX:
            arr[i] = arr[i-1]
            continue
        if a == 1:
            arr[i] = arr[i-1] + 1
            map_arr.append((arr[i], b))
        else:
            arr[i] = arr[i-1] * (b + 1)
            find_per[i] = per
            per = i
    queries = list(map(int, input().split()))
    # print("TEST")
    # print(arr)
    # print(map_arr)
    # print(find_per)
    ans = []
    for i in range(q):
        temp = bisect_left(arr, queries[i])
        if find_per[temp] == -1:
            found = True
            temp_ans = arr[temp]
        else:
            found = False
        if found == False:
            while True:
                if queries[i] % arr[temp-1] == 0:
                    queries[i] = arr[temp-1]
                else:
                    queries[i] = queries[i] % arr[temp-1]
                if find_per[temp] == None:
                    temp_ans = arr[temp - 1 - (arr[temp-1] - queries[i])]
                    break
                if temp - find_per[temp] > 1:
                    if arr[temp-1] - queries[i] + 1 <= temp - find_per[temp] - 1:
                        temp_ans = arr[temp - 1 - (arr[temp-1] - queries[i])]
                        break
                temp = find_per[temp]
        ans.append(temp_ans)
    # print(ans)
    ans = [map_arr[bisect_left(map_arr, (ans[i], 0))][1] for i in range(len(ans))]
    print(*ans)



for t in range(int(input())):
    solve()