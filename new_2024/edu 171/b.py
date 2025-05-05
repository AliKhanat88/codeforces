def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    if n == 1:
        print(1)
        return
    mini = 99999999999999999999999999
    if n % 2 == 1:
        for exclude in range(n):
            temp_arr = arr[:]
            temp_arr.pop(exclude)
            maxi = -1
            for i in range(1, len(temp_arr), 2):
                maxi = max(maxi, temp_arr[i] - temp_arr[i-1])
            # print(exclude, maxi)
            mini = min(mini, maxi)
    else:
        mini = -1
        for i in range(1, len(arr), 2):
            mini = max(mini, arr[i] - arr[i-1])
    print(mini)

for t in range(int(input())):
    solve()