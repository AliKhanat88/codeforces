import sys
input = sys.stdin.readline
from collections import defaultdict

inf = float("inf")

def get_mini(arr):
    mini1 = min(arr)
    mini1_index = arr.index(mini1)
    arr[mini1_index] = float("inf")
    mini2 = min(arr)
    mini2_index = arr.index(mini2)
    arr[mini1_index] = mini1
    return mini1, mini1_index, mini2, mini2_index
            

def solve(n, arr, tree):

    dfs = [(1, 0)]

    for cur, p in dfs:
        for child in tree[cur]:
            if child != p:
                dfs.append((child, cur))

    # print(dfs)

    dp = [0] *(n + 1)
    for cur, p in dfs[::-1]:
        temp_arr = [arr[cur] * (i + 1) for i in range(len(tree[cur]) + 1)]
        sumi = 0
        for child in tree[cur]:
            if child != p:
                sumi += dp[child][0]
                if dp[child][1] < len(temp_arr):
                    temp_arr[dp[child][1]] += (-dp[child][0] + dp[child][2])
        for i in range(len(temp_arr)):
            temp_arr[i] += sumi
        mini1, index1, mini2, index2 = get_mini(temp_arr)
        dp[cur] = [mini1, index1, mini2, index2]
    print(min(temp_arr))


for t in range(int(input())):
    n = int(input())
    arr = [0] + list(map(int, input().split()))

    tree = defaultdict(lambda: [])

    for i in range(n-1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
    solve(n, arr, tree)



