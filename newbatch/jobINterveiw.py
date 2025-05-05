def solve():
    n, m = map(int, input().split())

    arr = list(map(int, input().split()))

    brr= list(map(int, input().split()))

    p = 0
    t = 0
    for i in range(n+m+1):
        if arr[i] > brr[i]:
            p += 1
        else:
            t += 1
    ans = []
    if p > n:
        arr_ith = [None] * (n+m+1)
        k = 1
        sumi_first_n = 0
        other_tester = 0
        nplus = 0
        for i in range(n+m+1):
            if arr[i] > brr[i]:
                if k <= n:
                    sumi_first_n += arr[i]
                elif k == n+1:
                    nplus = (arr[i], brr[i])
                else:
                    other_tester += brr[i]
                if k <= n+1:
                    arr_ith[i] = k
                    k += 1
            else:
                other_tester += brr[i]
        # print(arr_ith, nplus)
        for i in range(n+m+1):
            if arr_ith[i] == None:
                ans.append(sumi_first_n + other_tester - brr[i] + nplus[1])
            else:
                ans.append(sumi_first_n + other_tester - arr[i] + nplus[0])

    elif t > m:
        arr_ith = [None] * (n+m+1)
        k = 1
        sumi_first_m = 0
        other_programmer = 0
        mplus = 0
        for i in range(n+m+1):
            if arr[i] < brr[i]:
                if k <= m:
                    sumi_first_m += brr[i]
                elif k == m+1:
                    mplus = (arr[i], brr[i])
                else:
                    other_programmer += arr[i]
                if k <= m+1:
                    arr_ith[i] = k
                    k += 1
            else:
                other_programmer += arr[i]
        # print(arr_ith)
        for i in range(n+m+1):
            if arr_ith[i] == None:
                ans.append(sumi_first_m + other_programmer - arr[i] + mplus[0])
            else:
                ans.append(sumi_first_m + other_programmer - brr[i] + mplus[1])
    print(*ans)
for t in range(int(input())):
    solve()