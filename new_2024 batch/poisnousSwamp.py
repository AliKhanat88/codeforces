def solve():
    n = int(input())
    arr = [0] * 2
    arr[0] = input()
    arr[1] = input()
    ans = 0
    for i in range(2):
        count = 0
        for j in range(n):
            if arr[i][j] == "*":
                count += 1
            else:
                ans = ans + max(0, (count - 1))
                count = 0
        ans = ans + max(0, (count - 1))
    print(ans)
for t in range(int(input())):
    solve()