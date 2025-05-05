from math import log2

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    # print("TEST")

    ans = 0
    arr[0] = [(arr[0] * (10 ** 10)) / (2 ** int(log2(arr[0]))), int(log2(arr[0]))]
    for i in range(1, n):
        
        arr[i] = [(arr[i] * (10 ** 10)) / (2 ** int(log2(arr[i]))), int(log2(arr[i]))]
        # print(arr)
        if arr[i][1] <= arr[i-1][1]:
            temp = arr[i-1][1] - arr[i][1]
            if arr[i][0] < arr[i-1][0]:
                temp += 1
            arr[i][1] += temp
            # print(temp, i)
            ans += temp
    print(ans)

for t in range(int(input())):
    solve()