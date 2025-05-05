def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    mini = n - 1
    for i in range(n-1, -1, -1):
        count = 1
        for j in range(i + 1, n):
            if arr[j] <= arr[i]:
                count += 1
        mini = min(mini, n - count)
    print(mini)
for t in range(int(input())):
    solve()