def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    if n == 1:
        print(0)
        return
    pos = 0
    neg = 0
    for i in range(n):
        if arr[i] < 0:
            neg += 1
        elif arr[i] > 0:
            pos += 1
    
    neg_max = min(arr)
    pos_max = max(arr)

    if abs(neg_max) >= abs(pos_max):
        if pos <= 12:
            done = False
        else:
            done = True
    else:
        if neg <= 12:
            done = True
        else:
            done = False
    if neg_max >= 0:
        done = True
    if pos_max <= 0:
        done = False

    # print(done)

    oper = []

    if done == True:
        temp_mini = arr.index(min(arr))
        temp_maxi = arr.index(max(arr))
        while abs(arr[temp_mini]) > arr[temp_maxi]:
            oper.append((temp_maxi + 1, temp_maxi + 1))
            arr[temp_maxi] += arr[temp_maxi]
        for i in range(1, n):
            if arr[i] < 0:
                temp_maxi = arr.index(max(arr))
                oper.append((i + 1, temp_maxi + 1))
                arr[i] += arr[temp_maxi]
                temp_maxi = arr.index(max(arr))
                oper.append((i + 1, temp_maxi + 1))
                arr[i] += arr[temp_maxi]
            elif arr[i] == 0:
                oper.append((i+1, i))
                arr[i] += arr[i-1]
            else:
                temp_maxi = arr.index(max(arr))
                oper.append((i + 1, temp_maxi + 1))
                arr[i] += arr[temp_maxi]
    else:
        temp_mini = arr.index(min(arr))
        temp_maxi = arr.index(max(arr))
        while abs(arr[temp_mini]) < arr[temp_maxi]:
            oper.append((temp_mini + 1, temp_mini + 1))
            arr[temp_mini] += arr[temp_mini]
        for i in range(n-2, -1, -1):
            if arr[i] > 0:
                temp_mini = arr.index(min(arr))
                oper.append((i + 1, temp_mini + 1))
                arr[i] += arr[temp_mini]
                temp_mini = arr.index(min(arr))
                oper.append((i + 1, temp_mini + 1))
                arr[i] += arr[temp_mini]
            elif arr[i] == 0:
                oper.append((i + 1, i+2))
                arr[i] += arr[i+1]
            else:
                temp_mini = arr.index(min(arr))
                oper.append((i + 1, temp_mini + 1))
                arr[i] += arr[temp_mini]
    if len(oper) > 31:
        # print(oper)
        raise Exception()
    print(len(oper))
    for op in oper:
        print(op[0], op[1])

for t in range(int(input())):
    solve()