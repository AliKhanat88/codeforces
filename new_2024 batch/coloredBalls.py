n = int(input())
selected = [0] * n
non = [0] * n
arr = list(map(int, input().split()))
non[0] = arr[0]
for i in range(1, n):
    for j in range(i, -1, -1):
        selected[j] = selected[j] * 2
        temp = abs(arr[i] - non[j])
        non[j] = temp
        selected[j] += min(arr[i], non[j]) * 2

print(sum(non) + sum(selected))