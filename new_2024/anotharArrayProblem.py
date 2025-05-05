def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    if n == 2:
        print(max(sum(arr), 2*abs(arr[0]-arr[1])))
    elif n == 3:
        print(max(sum(arr),arr[0] * 3, arr[2] * 3, 3 * abs(arr[0] - arr[2]), 3 * abs(arr[0] - arr[1]) , 3 * abs(arr[1] - arr[2])))
    else:
        print(max(arr) * n)

for t in range(int(input())):
    solve()