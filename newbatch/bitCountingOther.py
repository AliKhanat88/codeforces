def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    if n == 1:
        print(int("0" + "1" * arr[0], 2))
        return
    maxi = -1
    for i in range(1, n):
        if arr[i - 1] - arr[i] < -1:
            print(-1)
            return
        temp = "1" * (arr[i] - 1) + "0" + (arr[i-1] + 1 - arr[i]) * "1"

        maxi = max(maxi, int(temp, 2) - i + 1)
    # print(maxi)
    start = maxi
    for i in range(n):
        if bin(start).count("1") != arr[i]:
            print(-1)
            return
        start += 1
    print(maxi)



for t in range(int(input())):
    solve()