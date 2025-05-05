
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    maxi = arr[-1] - arr[0] + max(abs(arr[-1] - arr[-2]), abs(arr[0] - arr[1]))
    for i in range(1, n-1):
        maxi = max(maxi, arr[-1] - arr[i] + arr[i+1] - arr[i])
        maxi = max(maxi, arr[i] - arr[0] + arr[i] - arr[i-1])
    print(maxi)


for t in range(int(input())):
    solve()

