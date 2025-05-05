def solve():
    n, m ,k = map(int, input().split())
    arr = [*map(int, input().split())]
    arr.sort()
    sum_n = n
    i = 0
    while i < k and sum_n > 3:
        if (arr[i] // m) > 1:
            sum_n -= arr[i] // m
        i += 1
    if sum_n <= 0:
        print("YES")
        return
    if sum_n == 3:
        while i < k:
            if (arr[i] // m) > 2:
                print("YES")
                return
            i += 1
    elif sum_n in (2, 1):
        while i < k:
            if (arr[i] // m) > 1:
                print("YES")
                return
            i += 1 
    sum_m = m
    i = 0
    while i < k and sum_m > 3:
        if (arr[i] // n) > 1:
            sum_m -= arr[i] // n
        i += 1
    if sum_m <= 0:
        print("YES")
        return
    if sum_m == 3:
        while i < k:
            if (arr[i] // n) > 2:
                print("YES")
                return
            i += 1
    elif sum_m in (2, 1):
        while i < k:
            if (arr[i] // n) > 1:
                print("YES")
                return
            i += 1 
    print("NO")
for t in range(int(input())):
    solve()