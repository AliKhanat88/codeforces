def solve():
    n = int(input())
    p = list(map(int, input().split()))
    a = list(map(int, input().split()))
    arr = [0] * (n)
    for i in range(n):
        arr[i] = [p[i], a[i]]
    arr.sort()
    minus = 0
    for i in range(n):
        arr[i][1] -= minus
        if arr[i][1] < arr[i][0]:
            print(-1)
            return
        else:
            minus += (arr[i][1] - arr[i][0])
    print(minus)

for t in range(int(input())):
    solve()