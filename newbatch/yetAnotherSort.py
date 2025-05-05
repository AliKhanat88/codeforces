from collections import defaultdict

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    if len(set(arr)) != len(arr):
        print("YES")
        return

    temp = sorted(arr)
    dict = defaultdict(lambda:-1)
    for i in range(n):
        dict[arr[i]] = i
    ans = 0

    for i in range(n):
        if arr[i] != temp[i]:
            ans += 1
            temp_t = dict[temp[i]]
            dict[arr[i]] = temp_t
            arr[i], arr[temp_t] = arr[temp_t], arr[i]
    # print(arr)
    if ans % 2 == 0:
        print("YES")
    else:
        print("NO")



for t in range(int(input())):
    solve()