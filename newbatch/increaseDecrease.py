def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    ans = 1
    mini = float("inf")
    for i in range(n):
        ans += abs(arr[i] - brr[i])
        if arr[i] >= brr[i]:
            if brr[-1] <= arr[i] and brr[-1] >= brr[i]:
                mini = 0
            else:
                mini = min(mini, min(abs(brr[i] - brr[-1]) , abs(arr[i] - brr[-1])))
        else:
            if brr[-1] >= arr[i] and brr[-1] <= brr[i]:
                mini = 0
            else:
                mini = min(mini, min(abs(brr[i] - brr[-1]), abs(arr[i] - brr[-1])))

    print(ans + mini)

for t in range(int(input())):
    solve()