def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    can = True
    for i in range(1, n):
        if abs(arr[i] - arr[i-1]) not in (5, 7):
            can = False
    if can:
        print("YES")
    else:
        print("NO")
for t in range(int(input())):
    solve()