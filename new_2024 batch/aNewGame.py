from collections import defaultdict

n, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)

ans = 0
boss = 0

i = 0
while i < n:
    if boss >= 0:
        ans += boss
        boss += arr[i]
    else:
        break
    # print(ans, i)
    i += 1
dict = defaultdict(lambda:[])
j = 0
if boss < 0:
    dict[0].append(boss)
    j += 1

for i in range(i, n):
    j = j % (k + 1)
    dict[j].append(arr[i])
    j += 1
for i in range(k+1):
    start = 0
    for num in dict[i]:
        ans += start
        start += num

# print("TEST")
# print(arr)
# print(dict)
print(ans)