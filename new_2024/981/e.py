def solve():
    n = int(input())
    arr = [0] + list(map(int, input().split()))

    prr = [0] * (n+1)

    for i in range(1, n+1):
        prr[arr[i]] = i
    ans = 0
    # print(prr)
    # print(arr)
    for i in range(1, n+1):
        if arr[i] != i:
            if arr[arr[i]] != i:
                ans += 1
                # temp1 = prr[arr[i]]
                temp2 = prr[i]
                # print(arr[i], temp2)
                arr[arr[i]], arr[temp2] = arr[temp2], arr[arr[i]]
                prr[arr[temp2]] = temp2
        # print(arr)
    print(ans)
for t in range(int(input())):
    solve()