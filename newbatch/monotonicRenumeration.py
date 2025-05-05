n = int(input())
arr = list(map(int, input().split()))
# print(arr)
arr = [(arr[i], i) for i in range(n)]
arr.sort()
last = [-1] * n
for i in range(1, n):
    if arr[i][0] != arr[i-1][0]:
        for j in range(i-1, -1, -1):
            if arr[j][0] != arr[i-1][0]:
                break
            last[arr[j][1]] = max(last[arr[j][1]], arr[i-1][1])
for j in range(n-1, -1, -1):
    if arr[j][0] != arr[n-1][0]:
        break
    last[arr[j][1]] = max(last[arr[j][1]], arr[n-1][1])
# print(last)

maxi = -1
count = 0
for i in range(n):
    maxi = max(maxi, last[i])
    if i == maxi:
        count += 1
print(pow(2, count-1, 998244353))
            
    