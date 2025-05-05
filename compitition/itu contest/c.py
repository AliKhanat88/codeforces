from collections import defaultdict

def solve():
    dict = defaultdict(lambda:[])
    isdone = defaultdict(lambda:-1)
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    arr = [-1] * n 
    count = 0
    for i in range(n):
        if a[i] == b[i]:
            if arr[i] != -1:
                print(0)
                return
            arr[i] = a[i]
            count += 3
        if arr[a[i]] == -1:
            dict[a[i]].append(i)
        if arr[b[i]] == -1:
            dict[b[i]].append(i)
    for i in range(1, n):
        if len(dict[i]) == 0:
            print(0)
            return
        elif len(dict[i]) == 1:
            if arr[dict[i][0]] != -1:
                print(0)
                return
            else:
                arr[dict[i][0]] = i
        else:
            count += len(dict[i])
    print(count)


    print(dict)
for t in range(int(input())):
    solve()