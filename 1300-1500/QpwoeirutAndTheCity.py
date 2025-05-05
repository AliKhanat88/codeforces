def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    per = 0
    empty = [0] * n
    for i in range(n-2, 0, -2):
        empty[i] = per =  max(max(arr[i-1], arr[i+1]) - arr[i] + 1, 0) + per
    if (n - 2) % 2 == 1:
        print(empty[1])
        return
    
    per = 0
    for i in range(1, n-1, 2):
        empty[i] = per = max(max(arr[i-1], arr[i+1]) - arr[i] + 1, 0) + per
    mini = empty[2]
    for i in range(1, n-3, 2):
        mini = min(mini, empty[i] + empty[i+3])
    print(min(mini, empty[n-3]))

for t in range(int(input())):
    solve()