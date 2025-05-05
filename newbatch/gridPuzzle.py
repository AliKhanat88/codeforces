inf = 9999999999999999999999
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    if n == 1:
        if arr[0] == 0:
            print(0)
        else:
            print(1)
        return
    arr = [0] + arr
    mini = [inf] * (n+1)
    mini[0] = 0
    if arr[1] >= 5:
        row1 = None
    else:
        row1 = [0] * 4
        for i in range(4):
            if i+1 <= arr[1]:
                row1[i] = 1
    # print("TEST")
    # print(arr)
    # print(row1)
    for i in range(1, n):
        if arr[i] == 0:
            mini[i] = min(mini[i], mini[i-1])
            if arr[i+1] >= 3:
                row1 = None
            else:
                row1 = [0] * 4
                for j in range(4):
                    if j+1 <= arr[i+1]:
                        row1[j] = 1
        elif arr[i] >= 5 or row1 == None or row1.count(1) > 2:
            mini[i] = min(mini[i], mini[i-1] + 1)
            if arr[i+1] >= 5:
                row1 = None
            else:
                row1 = [0] * 4
                for j in range(4):
                    if j+1 <= arr[i+1]:
                        row1[j] = 1
        else:
            if row1.count(1) == 0:
                mini[i] = mini[i-1]
                if arr[i+1] >= 5:
                    row1 = None
                else:
                    row1 = [0] * 4
                    for j in range(4):
                        if j+1 <= arr[i+1]:
                            row1[j] = 1
            elif arr[i+1] >= 5 or arr[i+1] == 0:
                row1 = None
                mini[i] = mini[i-1] + 1
            else:
                row2 = [0] * 4
                for j in range(4):
                    if j+1 <= arr[i+1]:
                        row2[j] = 1
                for j in range(4):
                    if row1[j] == 1:
                        row1[j] = 0
                        row1[j+1] = 0
                        row2[j] = 0
                        row2[j+1] = 0
                # print(i)
                mini[i] = min(mini[i], mini[i-1] + 1)
                row1 = row2
    # print(row1)
    if arr[-1] == 0:
        print(mini[n-1])
    elif row1 == None:
        print(mini[n-1] + 1)
    else:
        if row1.count(1) == 0:
            print(mini[n-1])
        else:
            print(mini[n-1] + 1)

    # print(mini)                    



for t in range(int(input())):
    solve()