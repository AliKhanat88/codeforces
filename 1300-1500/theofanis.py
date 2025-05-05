def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    arr_sum = [0] * n
    arr_sum[-1] = arr[-1]
    for i in range(n-2, -1, -1):
        arr_sum[i] = arr[i] + arr_sum[i+1]

    sumi = arr[0]
    count = 1
    for i in range(1,n):
        if arr_sum[i] > 0:
            count += 1
            sumi += count * arr[i]
        else:
            sumi += count * arr[i]
    # print(arr_sum)
    print(sumi)

for t in range(int(input())):
    solve()