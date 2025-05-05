from math import log2

def solve():
    n = int(input())
    arr = [*map(int, input().split())]
    count = 0
    for i in range(n):
        while arr[i] % 2 == 0:
            count += 1
            arr[i] = arr[i] // 2
    count_arr = [0]*(n//2+1)
    k = 0
    for i in range(2, n+1, 2):
        while i % 2 == 0:
            count_arr[k] += 1
            i = i // 2
        k += 1
    count_arr.sort(reverse=True)
    i = 0
    ans = 0
    # print(count_arr)
    while count < n and i < len(count_arr):
        count += count_arr[i]
        ans += 1
        i += 1
    if count < n:
        print(-1)
    else:
        print(ans)
for t in range(int(input())):
    solve()
