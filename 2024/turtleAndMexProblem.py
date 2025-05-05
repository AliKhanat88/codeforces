import sys
input = sys.stdin.readline
from bisect import insort_left
from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    count_first = defaultdict(lambda: 0)
    scn_map = defaultdict(lambda:[])
    length = -1
    maxi_first = -1
    for i in range(n):
        arr = list(map(int, input().split()))
        length = max(length, arr.pop(0))
        arr.sort()
        # Initialize mex to 0
        mex = 0

        # Iterate through the sorted array
        for num in arr:
            if num == mex:
                mex += 1
            elif num > mex:
                break
        count_first[mex] += 1
        maxi_first = max(maxi_first, mex)
        temp1 = mex
        insort_left(arr, mex)
        mex = 0
        for num in arr:
            if num == mex:
                mex += 1
            elif num > mex:
                break
        scn_map[mex].append(temp1)
    # print(scn_map)
    default = -1
    dp = [-1] * (length+2)
    i = length + 1
    while i > -1:
        if dp[i] == -1:
            stack = [i]
            while len(stack) != 0:
                cur = stack.pop()
                if dp[cur] != -1:
                    continue
                if count_first[cur] > 1:
                    default = i
                    break
                for child in scn_map[cur]:
                    stack.append(child)
                dp[cur] = i
        if default != -1:
            break
        i -= 1
    # print(default)
    # print(dp)
    ans = 0
    i = 0
    while i <= min(m, length + 1):
        ans = ans + max(default, dp[i], maxi_first)
        i += 1
    if m > length + 1:
        ans = ans + ((length + 2 + m) * (m - (length + 1)) // 2)

    print(ans)


for t in range(int(input())):
    solve()