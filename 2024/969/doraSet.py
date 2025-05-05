def solve():
    l, r = map(int, input().split())
    temp = r - l + 1
    if l % 2 == 1:
        temp += 1
    print((temp // 2) // 2)

for t in range(int(input())):
    solve()