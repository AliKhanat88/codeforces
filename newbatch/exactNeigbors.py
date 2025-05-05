from collections import Counter

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    c = Counter(arr)
    for i in range(n):
        arr[i] = [arr[i], i]
    ans = [0] * n
    if c[0] >= 1:
        for i in range(n):
            if arr[i][0] == 0:
                arr[0], arr[i] = arr[i], arr[0]
                break
        start = 1
        ans[0] = (1, 1, arr[0][1])
    else:
        done = False
        for i in range(n+1):
            if c[i] > 1:
                done = True
                for j in range(n):
                    if arr[j][0] == i:
                        arr[0], arr[j] = arr[j], arr[0]
                        break
                for j in range(1,n):
                    if arr[j][0] == i:
                        arr[1], arr[j] = arr[j], arr[1]
                        break
                break
        if done == True:
            start = 1
            ans[0] = (1, 1, arr[1][1])
        else:
            if n == 2:
                print("NO")
                return
            arr = sorted(arr, key=lambda x:x[0])
            ans[0] = [1, 1, arr[1][1]]
            ans[1] = [1, 2, arr[2][1]]
            start = 2
    for i in range(start, n):
        ans[i] = [1, i+1, arr[i][1]]
        if arr[i][0] < i:
            ans[i] = (ans[i - arr[i][0]][0] ,i + 1, arr[i - arr[i][0]][1])
        else:
            ans[i] = (arr[i][0] - i + 1, i + 1, arr[0][1])
    new_ans = [0] * n
    for i in range(n):
        new_ans[arr[i][1]] = ans[i]
    print("YES")
    for i in range(n):
        print(new_ans[i][1], new_ans[i][0])
    print(*[new_ans[i][2] + 1 for i in range(n)])
    

solve()