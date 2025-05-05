from pprint import pprint
n = int(input())
a = list(map(int, input().split()))
arr = [[0] * i for i in range(1, n+1)]

def recur(i, j, val, count):
    if count == 1:
        arr[i][j] = val
        return
    else:
        # print(arr,i, j, count)
        arr[i][j] = val
        if j-1 >= 0 and arr[i][j-1] == 0:
            recur(i, j-1, val, count-1)
        elif i+1 < n and arr[i+1][j] == 0:
            recur(i+1, j, val, count-1)
        elif i-1 >= 0 and arr[i-1][j] == 0:
            recur(i-1, j, val, count-1)
        elif j+1 < len(arr[i]) and arr[i][j+1] == 0:
            recur(i, j + 1, val, count-1)
        else:
            print(-1)
            exit()


for i in range(n):
    recur(i, i, a[i], a[i])

for i in range(n):
    print(" ".join([str(num) for num in arr[i]]))
# pprint(arr)