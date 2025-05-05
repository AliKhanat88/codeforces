def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()

    maxieven = -1
    maxiodd = -1
    for i in range(n):
        if arr[i] % 2 == 1:
            maxiodd = max(maxiodd, arr[i])
        else:
            maxieven = max(maxieven, arr[i])
    if maxiodd == -1:
        print(0)
        return
    ans = 0
    for i in range(n):
        if arr[i] % 2 == 0:
            if maxiodd > arr[i]:
                ans += 1
                maxiodd += arr[i]
            else:
                ans += 2
                maxiodd += arr[i] + maxieven
    print(ans)


for t in range(int(input())):
    solve()