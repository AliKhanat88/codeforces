def solve():
    n, m = map(int, input().split())
    if n > m:
        print(0)
        return
    arr = []
    for b in range(31):
        if (2 ** b) & n == 0:
            arr.append(2 ** b)
    lower = 1
    upper = 2 ** (len(arr)) - 1

    while lower + 1 < upper:
        mid = lower + (upper - lower) // 2
        temp = 0
        for b in range(len(arr)):
            if (2 ** b) & mid != 0:
                temp += arr[b]
        if temp + n > m:
            upper = mid
        elif temp + n <= m:
            lower = mid + 1
    temp = 0
    for b in range(len(arr)):
            if (2 ** b) & lower != 0:
                temp += arr[b]
    if temp + n > m:
        print(temp)
        return
    temp = 0
    for b in range(len(arr)):
            if (2 ** b) & upper != 0:
                temp += arr[b]
    print(temp)
for t in range(int(input())):
    solve()