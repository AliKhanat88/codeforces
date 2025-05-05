def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    arr = [arr[i % n] for i in range(-1, n-1)]
    print(*arr)

for t in range(int(input())):
    solve()
