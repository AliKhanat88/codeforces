def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    prepareTime = list(map(int, input().split()))
    maxi = arr[0]
    mini = arr[0]
    for i, num in enumerate(arr):
        mini = min(mini, arr[i] - prepareTime[i])
        maxi = max(maxi, arr[i] + prepareTime[i])
    # print(mini, maxi)
    print(mini + (maxi - mini) / 2)
for t in range(int(input())):
    solve()