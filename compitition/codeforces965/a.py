def solve():
    xc, yc, k = map(int, input().split())
    if xc == 0 and yc == 0 and k % 2 == 0:
        pass
    elif k % 2 == 1:
        print(k * xc,k * yc)
        k -= 1
    else:
        print(k * xc, k *yc)
        print(0, 0)
        k -= 2
    start = 10 ** 9
    for i in range(k // 2):
        print(start, start)
        print(-start, -start)
        start -= 1

for t in range(int(input())):
    solve()