def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    per = 0
    total = 0
    for i in range(1, n):
        if 2 * arr[i] > arr[i-1]:
            per += 1
            if per == k:
                per -= 1
                total += 1

        else:
            per = 0
    print(total)
for t in range(int(input())):
    solve()