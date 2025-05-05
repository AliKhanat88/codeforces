import sys
input = sys.stdin.readline

n, q = map(int, input().split())
arr = list(map(int, input().split())) 
if n <= 2:
    for i in range(q):
        a, b = map(int, input().split())
        print(b-a+1)
else:
    count_arr = [0] * n
    count_arr[0] = 1
    count_arr[1] = 2
    per = 2
    for i in range(2, n):
        if arr[i] <= arr[i-1] and arr[i-1] <= arr[i-2]:
            count_arr[i] = per
        else:
            per += 1
            count_arr[i] = per

    # print(count_arr)
    for i in range(q):
        a, b = map(int, input().split())
        print(count_arr[b-1] - count_arr[a-1] + 1)
