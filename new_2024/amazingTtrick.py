def solve(n, arr):
    # print("TESTt")
    doubles = set()
    singles = []
    for i in range(1, n+1):
        if arr[i] != i and arr[arr[i]] == i:
            if (arr[i], i) not in doubles and (i, arr[i]) not in doubles:
                doubles.add((i, arr[i]))
        else:
            singles.append(i)
    # print(doubles)
    # print(singles)
    if len(doubles) == 1 and len(singles) <= 1 or n == 1:
        print("Impossible")
        return
    new_arr = arr[:]
    doubles = list(doubles)
    if len(doubles) > 1:
        for i in range(1, len(doubles)):
            temp1, temp2 = new_arr[doubles[i][0]], new_arr[doubles[i][1]]
            new_arr[doubles[i][0]], new_arr[doubles[i][1]] = new_arr[doubles[i-1][0]], new_arr[doubles[i-1][1]]
            new_arr[doubles[i-1][0]], new_arr[doubles[i-1][1]] = temp1, temp2
    elif len(doubles) == 1:
        temp1, temp2 = new_arr[doubles[0][0]], new_arr[doubles[0][1]]
        new_arr[doubles[0][0]], new_arr[doubles[0][1]] = new_arr[singles[0]], new_arr[singles[1]]
        new_arr[singles[0]], new_arr[singles[1]] = temp1, temp2
    # print(new_arr)
    # print(doubles)
    if new_arr[1] == 1:
        new_arr[1], new_arr[-1] = new_arr[-1], new_arr[1]
    for i in range(2, n+1):
        if new_arr[i] == i:
            new_arr[i], new_arr[1] = new_arr[1], new_arr[i]
    # print(arr)
    # print(new_arr)
    index_arr = [0] * (n+1)
    index_new_arr = [0] * (n + 1)
    for i in range(1, n+1):
        index_arr[arr[i]] = i
        index_new_arr[new_arr[i]] = i

    q = [0] * (n + 1)
    for i in range(1, n+1):
        q[i] = index_new_arr[index_arr[i]]
    print("Possible")
    print(*new_arr[1:])
    print(*q[1:])
    for i in range(1, n+1):
        if new_arr[i] == i or q[i] == i or arr[new_arr[q[i]]] != i:
            raise("Exception")




# import random
# for i in range(10000):
#     n = 5
#     arr = [0] + random.sample([i for i in range(1, n+1)], n)
#     print(arr)
#     solve(n, arr)

for t in range(int(input())):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    solve(n,arr)