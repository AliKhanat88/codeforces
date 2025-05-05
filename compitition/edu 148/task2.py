def print_max(n, k, temp_arr):
    temp_arr.sort()
    arr = [0] * n
    arr[0] = temp_arr[0]
    for i in range(1, n):
        arr[i] = arr[i-1] + temp_arr[i]
    j = n - 1
    k = 2 * k
    # print(arr)
    mini = 999999999999999999999999999999999999999
    first = 0
    last = n
    for i in range(k-1, -1, -2):
        temp = arr[i] + arr[-1] - arr[j]
        if temp < mini:
            mini = temp
            first = i
            last = j
        j -= 1
    if arr[-1] - arr[j] < mini:
        first = -1
        last = j
    print(sum(temp_arr[first+1:last+1]))
for t in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print_max(n, k, arr)