from bisect import bisect_right

def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    if n == k:
        print(10 ** 9)
        return
    sorted_arr = sorted([(arr[i], i) for i in range(n)])

    # print(sorted_arr, "sorted_Arr")

    # for 0
    temp_arr = arr[:]
    for i in range(k):
        temp_arr[sorted_arr[i][1]] = 10 ** 9
    
    # print(temp_arr, "temp_arr")

    temp_maxi = -1
    temp = -1
    for i in range(n):
        temp_maxi = max(temp_maxi, min(temp, temp_arr[i]))
        temp = temp_arr[i]
    
    # print(temp_maxi, "temp_maxi")
    maxi = min(2 * min(temp_arr), temp_maxi)
    # print(maxi, "first maxi")

    for i in range(n):
        cur_maxi = -1
        if i - 1 >= 0:
            cur_maxi = max(cur_maxi, arr[i-1])
        if i + 1 < n:
            cur_maxi = max(cur_maxi, arr[i+1])

        index = min(k-1, bisect_right(sorted_arr, (cur_maxi, 10 * 5 + 1)))
        if sorted_arr[index][0] >= arr[i]:
            index += 1
        maxi = max(maxi , min(cur_maxi, sorted_arr[index][0] * 2))

    # print(maxi, "maxi after 1 op")
    
    if k <= 1:
        print(maxi)
        return
    for i in range(1, n):
        mini1 = min(arr[i], arr[i-1])
        mini2 = max(arr[i], arr[i-1])
        index = k - 2
        if sorted_arr[index][0] >= mini1:
            index += 1
        if sorted_arr[index][0] >= mini2:
            index += 1
        maxi = max(maxi, min( 10 ** 9, sorted_arr[index][0] * 2))
    print(maxi)

for t in range(int(input())):
    solve()