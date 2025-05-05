def solve():
    n, k, d = map(int, input().split())

    arr = list(map(int ,input().split()))

    arr_i = list(map(int, input().split()))
    # print("TEST")
    # print(arr)
    # print(arr_i)
    maxi = -999999
    i = 0
    while i < 2 * n and i < d:
        sumi = 0
        for j in range(n):
            if arr[j] == (j+1):
                sumi += 1
        # print(i, sumi)
        if sumi + ((d - (i+1)) // 2) > maxi:
            maxi = sumi + ((d - (i+1)) // 2)
        i += 1

        for j in range(arr_i[(i-1) % k]):
            arr[j] += 1
        # print(i)
    # print("TEST")
    print(maxi)



for t in range(int(input())):
    solve()