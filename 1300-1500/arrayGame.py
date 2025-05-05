from bisect import bisect_right

def solve():
    n, k = map(int, input().split())
    arr = [*map(int, input().split())]

    if k == 1:
        mini = 99999999999999999999999999999999999999999
        for j in range(len(arr)):
            for l in range(j+1, len(arr)):
                mini = min(mini, abs(arr[j] - arr[l]))
        print(min(mini, min(arr)))
    elif k == 2:
        sort_arr = sorted(arr)
        mini = 99999999999999999999999999999999999999999
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                # print(i,j)
                temp = abs(arr[i] - arr[j])
                mini = min(mini, temp)
                temp1 = bisect_right(sort_arr, temp)
                mini = min(mini, abs(temp - sort_arr[temp1]))
                if temp1 > -1:
                    mini = min(mini, abs(temp - sort_arr[temp1-1]))
                # print(temp, temp1)
        print(min(mini, min(arr)))
    else:
        print(0)
        


for t in range(int(input())):
    solve()