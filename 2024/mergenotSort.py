
def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    arr_block = []
    block = [arr[0]]
    maxi = arr[0]
    for i in range(1, 2 * n):
        if arr[i] > maxi:
            arr_block.append(block)
            block = []
            maxi = arr[i]
        block.append(arr[i])
    if len(block) != 0:
        arr_block.append(block)
    # print(arr_block)
    len_arr = [len(arr_block[i]) for i in range(len(arr_block))]
    dp = [-1] * (n + 1)
    for i in range(len(arr_block)):
        
        for j in range(n, 0, -1):
            if dp[j] != -1 and j + len_arr[i] <= n and dp[j + len_arr[i]] == -1:
                dp[j + len_arr[i]] = (j, i)
        if len_arr[i] <= n and dp[len_arr[i]] == -1:
            dp[len_arr[i]] = (-1, i)

    # print(dp)
    if dp[-1] == -1:
        print(-1)
        return
    p1 = []
    point = n
    while point != -1:
        temp = dp[point][1]
        for j in range(len_arr[temp]-1, -1, -1):
            p1.append(arr_block[temp][j])
        point = dp[point][0]
    # print(p1)
    seti = set(p1)
    p2 = []
    for i in range(2*n):
        if arr[i] not in seti:
            p2.append(arr[i])
    print(*p1[::-1])
    print(*p2)
    
solve()