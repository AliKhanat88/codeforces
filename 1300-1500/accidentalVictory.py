from collections import defaultdict

def solve():
    n = int(input())
    new_arr = list(map(int, input().split()))
    dict = defaultdict(lambda:False)
    arr = sorted(new_arr)
    arr_sum = [0] * n
    arr_sum[0] = arr[0]
    for i in range(1, n):
        arr_sum[i] = arr_sum[i-1] + arr[i]

    count = 1
    dict[arr[-1]] = True
    for i in range(n-2, -1, -1):
        if arr[i+1] > arr_sum[i]:
            break
        else:
            dict[arr[i]] = True
            count += 1

    # print(dict)
    print(count)
    for i in range(n):
        if dict[new_arr[i]]:
            print(i+1, end=" ")
    print()

for t in range(int(input())):
    solve()