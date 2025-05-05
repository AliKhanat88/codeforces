def solve():
    n = int(input())
    arr = []
    arr.append(input())
    arr.append(input())
    total = arr[0].count(".") + arr[1].count(".")
    if total <= 2:
        print(0)
        return
    i = 0
    start = 0
    while i < n:
        if arr[0][i] == "." or arr[1][i] == ".":
            start = i + 1
            break
        i += 1
    last = 0
    i = n-1
    while i >= 0:
        if arr[0][i] == "." or arr[1][i] == ".":
            last = i - 1
            break
        i -= 1
    ans = 0
    for i in range(start, last + 1):
        if arr[0][i] == "." and arr[1][i-1] == "x" and arr[1][i] == "." and arr[1][i+1] == "x":
            ans += 1

    for i in range(start, last + 1):
        if arr[1][i] == "." and arr[0][i-1] == "x" and arr[0][i] == "." and arr[0][i+1] == "x":
            ans += 1
    print(ans)


for t in range(int(input())):
    solve()