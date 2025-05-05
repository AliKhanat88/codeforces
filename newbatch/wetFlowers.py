n, p = map(int, input().split())
arr = [0] * n
for i in range(n):
    a, b = map(int, input().split())
    arr[i] = [b - a + 1, max(0, b // p - (a-1) // p )]

# print(arr)
ans = 0
for i in range(1, n-1):
    ans += ((arr[i][1] * arr[i-1][0] + (arr[i][0] - arr[i][1]) * arr[i-1][1]) * 1000) / (arr[i][0] * arr[i-1][0])
    ans +=  ((arr[i][1] * arr[i+1][0] + (arr[i][0] - arr[i][1]) * arr[i+1][1]) * 1000) / (arr[i][0] * arr[i+1][0])
ans += ((arr[-1][1] * arr[-2][0] + (arr[-1][0] - arr[-1][1]) * arr[-2][1]) * 1000) / (arr[-1][0] * arr[-2][0])
ans += ((arr[-1][1] * arr[0][0] + (arr[-1][0] - arr[-1][1]) * arr[0][1]) * 1000) / (arr[-1][0] * arr[0][0])
ans += ((arr[0][1] * arr[-1][0] + (arr[0][0] - arr[0][1]) * arr[-1][1]) * 1000) / (arr[0][0] * arr[-1][0])
ans += ((arr[0][1] * arr[1][0] + (arr[0][0] - arr[0][1]) * arr[1][1]) * 1000) / (arr[0][0] * arr[1][0])

print(ans)