def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    brr = [0] + arr
    for i in range(1, n):
        brr[i-1] = brr[i] | brr[i-1]
    
    for i in range(1, n):
        if brr[i] & brr[i-1] != arr[i-1]:
            print(-1)
            return
    print(*brr)

for t in range(int(input())):
    solve()