from heapq import heappop, heappush, heapify
def solve():
    n, m = map(int, input().split())
    arr = input().split()
    total = 0
    # if len(arr) == 1 and int(arr[0]) == 1 and m == 0:
    #     print("Sasha")
    #     return
    # print(arr)
    for i in range(n):
        total += len(arr[i])
        j = len(arr[i]) - 1
        temp = 0
        while j >= 0:
            if arr[i][j] == "0":
                temp += 1
            else:
                break
            j -= 1
        arr[i] = -temp
    
    # print(total)
    # print(arr)
    heapify(arr)

    isAnna = True
    while len(arr) != 0:
        temp = heappop(arr)
        if isAnna:
            total += temp
        isAnna = not isAnna
    if total > m:
        print("Sasha")
    else:
        print("Anna")
    # print(total, m)


for t in range(int(input())):
    solve()