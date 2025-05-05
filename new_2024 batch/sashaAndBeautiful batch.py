def solve():
    n = int(input())
    arr = [*map(int, input().split())]
    print(max(arr) - min(arr))



for t in range(int(input())):
    solve()