def solve():
    n, k = map(int, input().split())

    arr = list(map(int, input().split()))

    arr.sort()
    # print("TEST")
    # print(arr, k)
    i = 1
    mini = arr[0]
    while i < n and k > 0:
        if arr[i] - arr[i-1] > 0:
            op = min(k // i, arr[i] - arr[i-1])
            k = k - (op * i)
            arr[i-1] += op
            mini = mini + op
            # print("op,k,i, mini", op, k, i, mini)
        i += 1
    if k > 0 and i >= n:
        op = k // n
        k = k - (op * n)
        mini += op
    # print(mini, i, k)
    # print(arr)
    ans = mini * n - n + 1

    # print("pre", ans)
    for j in range(n-1, -1, -1):
        if arr[j] > mini:
            ans += 1
        elif k > 0:
            ans += 1
            k -= 1
    print(ans)

for t in range(int(input())):
    solve()