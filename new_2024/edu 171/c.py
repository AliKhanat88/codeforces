from collections import deque

def solve():
    n = int(input())
    arr = list(map(int, list(input())))
    if n == 1:
        print(1)
        return
    sumi = (n * (n + 1)) // 2
    # ones = [0] * n
    # per = 0
    # for i in range(n):
    #     if arr[i] == 1:
    #         ones[i] = per + 1
    #     else:
    #         ones[i] = per
    #     per = ones[i]
    
    # print(ones)
    temp_ones = 0
    sumi_ones = 0
    mini = sumi - n
    for i in range(n - 1, -1, -1):
        if arr[i] == 1:
            temp_ones += 1
            sumi_ones += (i + 1)
            if i - temp_ones >= 0:
                mini = min(mini, sumi - sumi_ones)
        else:
            temp_ones -= 1
            temp_ones = max(0, temp_ones)
        # print(sumi_ones, temp_ones, i + 1, mini)
    print(mini)





for t in range(int(input())):
    solve()