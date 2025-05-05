def solve():
    n = int(input())

    arr = list(map(int, input().split()))

    maxi = 99999999999999999999999999999

    for i in range(1, n):
        maxi = min(maxi, max(arr[i], arr[i-1]) - 1)

    print(maxi)

for t in range(int(input())):
    solve()