def solve():
    n = int(input())

    arr = list(map(int, input().split()))

    for i in range(n):
        if arr[arr[i] - 1] == i + 1:
            print(2)
            return 
        
    print(3)
for t in range(int(input())):
    solve()