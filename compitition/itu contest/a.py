n = int(input())
arr = [0] * n
for i in range(n):
    a, b = map(int, input().split())
    arr[i] = (a, b)
# print(arr)

count = 0
for i in range(n):
    left = False
    right = False
    up = False
    down = False
    for j in range(n):
        if i != j:
            if arr[j][0] > arr[i][0] and arr[j][1] == arr[i][1]:
                right = True
            elif arr[j][0] < arr[i][0] and arr[j][1] == arr[i][1]:
                left = True
            elif arr[j][0] == arr[i][0] and arr[j][1] > arr[i][1]:
                up = True
            elif arr[j][0] == arr[i][0] and arr[j][1] < arr[i][1]:
                down = True
    if left == True and right == True and up == True and down == True:
        count += 1
        # print(arr[i])
print(count)