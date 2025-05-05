def solve():
    n, m, k = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    ans = 0
    for num in arr2:
        for num2 in arr1:
            if num + num2 <= k:
                ans += 1
    print(ans)

for t in range(int(input())):
    solve()