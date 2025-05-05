def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    sumi = 0
    count = 0
    for i in range(n):
        if arr[i] >= k :
            sumi += arr[i]
        elif arr[i] == 0 and sumi > 0:
            sumi -= 1
            count += 1

    print(count)

for t in range(int(input())):
    solve()