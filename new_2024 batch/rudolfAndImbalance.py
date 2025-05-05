def solve():
    n,m,k = map(int, input().split())

    arr = list(map(int, input().split()))

    arr_d = list(map(int, input().split()))

    arr_f = list(map(int, input().split()))

    maxi = arr[1] - arr[0]
    maxi1 = arr[0]
    maxi2 = arr[1]
    for i in range(2, n):
        if arr[i] - arr[i-1] > maxi:
            maxi = arr[i] - arr[i-1]
            maxi1 = arr[i-1]
            maxi2 = arr[i]


    check1 = maxi1 + maxi // 2
    check2 = maxi2 - maxi // 2

    arr_f.sort()

    # print("TEST")
    # print(f"maxi: {maxi}, maxi1: {maxi1}, maxi2: {maxi2}, check1: {check1}, check2:{check2}")
    # print(arr)
    # print(arr_d)
    # print(arr_f)
    miniFound = maxi
    for num in arr_d:
        lower = 0
        upper = k-1
        isFound = False
        while upper - lower > 1:
            mid = lower + (upper - lower) // 2
            if num + arr_f[mid] == check1 or num + arr_f[mid] == check2:
                isFound = True
                break
            elif num + arr_f[mid] < check1:
                lower = mid
            elif num + arr_f[mid] > check2:
                upper = mid
        # print(isFound)
        if isFound == True:
            miniFound = max(num + arr_f[mid] - maxi1,maxi2 - (num + arr_f[mid]))
            break
        if arr_f[upper] + num > maxi1 and arr_f[upper] + num < maxi2 and max(num + arr_f[upper] - maxi1,maxi2 - (num + arr_f[upper])) < miniFound:
            miniFound = max(num + arr_f[upper] - maxi1,maxi2 - (num + arr_f[upper]))
        if arr_f[lower] + num > maxi1 and arr_f[lower] + num < maxi2 and max(num + arr_f[lower] - maxi1,maxi2 - (num + arr_f[lower])) < miniFound:
            miniFound = max(num + arr_f[lower] - maxi1,maxi2 - (num + arr_f[lower]))
        # print(f"num: {num}, lower: {arr_f[lower]}, upper: {arr_f[upper]}, miniFound: {miniFound}")
    # print(miniFound, maxi)
    if miniFound >= maxi:
        print(maxi)
        return
    maxi = -1
    for i in range(1, n):
        if arr[i] == maxi2 and arr[i-1] == maxi1:
            continue
        if arr[i] - arr[i-1] > maxi:
            maxi = arr[i] - arr[i-1]
    print(max(maxi, miniFound))

for t in range(int(input())):
    solve()