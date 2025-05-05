def solve():
    x, y, k = map(int, input().split())
    temp_k = min(x, y)
    print(0, 0, temp_k, temp_k)
    print(0, temp_k, temp_k, 0)

for t in range(int(input())):
    solve()