def solve():
    a, b = map(int, input().split())

    if b % 2 == 1:
        temp1 = b // 2 + 1
        a = a - (b // 2) * 7 - 11
    else:
        temp1 = b // 2
        a = a - (b // 2) * 7
    if max(0, a) % 15 == 0:
        temp2 = max(0, a) // 15
    else:
        temp2 = max(0, a) // 15 + 1
    print(temp1 + temp2)

for t in range(int(input())):
    solve()