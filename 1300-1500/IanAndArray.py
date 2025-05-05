def solve():
    # print("TEST")
    n = int(input())
    arr = list(map(int, input().split()))
    if n % 2 == 1:
        print("YES")
        return
    else:
        for i in range(1, n-1):
            diff = arr[i-1] - arr[i]
            arr[i] = arr[i-1]
            arr[i+1] = arr[i+1] + diff

    # print(arr)
    if arr[-1] >= arr[-2]:
        print("YES")
    else:
        print("NO")

for t in range(int(input())):
    solve()