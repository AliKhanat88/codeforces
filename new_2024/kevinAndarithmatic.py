def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    count = 0
    for i in range(n):
        if arr[i] % 2 == 0:
            count += 1
    
    if count > 0:
        print(n - count + 1)
    else:
        print(n - 1)

for t in range(int(input())):
    solve()