def solve():
    n = int(input())

    arr = list(map(int, input().split()))

    # print("TEST")
    # print(arr)
    # down
    down = [0] * (n + 1)
    i = 0 
    per = 0
    while i < n:
        if arr[i] >= per:
            down[i+1] = down[i] + 1
        else:
            down[i+1] = down[i]
        per = arr[i]
        i += 1
    # print(down)
    # up
    up = [0] * (n+1)
    i = 0
    per = 0
    while i < n:
        if arr[i] <= per:
            up[i+1] = up[i] + 1
        else:
            up[i+1] = up[i]

        per = arr[i]
        i += 1

    # print(up)
    mini = down[-1]
    for i in range(n):
        mini = min(down[i] + up[-1] - up[i+1], mini)
    print(mini)
for t in range(int(input())):
    solve()


