from collections import defaultdict
import sys
input = sys.stdin.readline
from random import randint, choice
from itertools import permutations
from copy import deepcopy
from math import log2, ceil

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
                temp_arr[dp[child][1]] += (-dp[child][0] + dp[child][2])
        for i in range(len(temp_arr)):
            temp_arr[i] += sumi
        mini1, index1, mini2, index2 = get_mini(temp_arr)
        dp[cur] = [mini1, index1, mini2, index2]
    print(min(temp_arr))
    


# for t in range(int(input())):
#     n = int(input())
#     arr = [0] + list(map(int, input().split()))

#     tree = defaultdict(lambda: [])

#     for i in range(n-1):
#         a, b = map(int, input().split())
#         tree[a].append(b)
#         tree[b].append(a)
#     solve(n, arr, tree)


def make_graph(n):
    seti = [1]

    tree = defaultdict(lambda: [])
    for i in range(1, n):
        while True:
            temp = randint(1, n)
            if temp not in seti:
                ch = choice(seti)
                tree[ch].append(temp)
                tree[temp].append(ch)
                seti.append(temp)
                break
            # print(seti)

    return tree

def brute(n, arr, tree):
    if n == 1:
        print(sum(arr))
        return
    elif n == 2:
        print(sum(arr) + min(arr[1:]))
    max_len = int(log2(n)) + 3

    stack = [(1, 0)]
    children = [0] * (n +1)
    parent = [-1] * (n + 1)

    leaves = []
    visited = [False] * (n + 1)
    while len(stack):
        cur = stack.pop()
        parent[cur[0]] = cur[1]
        visited[cur[0]] = True
        can = False
        for child in tree[cur[0]]:
            if not visited[child]:
                stack.append((child, cur[0]))
                children[cur[0]] += 1
                can = True
        if not can:
            leaves.append(cur[0])
    # print(parent)

    # print(children)

    dp = [[] for i in range(n+1)]

    while len(leaves):
        cur = leaves.pop()
        if cur == 0:
            break
        if len(dp[cur]) == 0:
            cur_state = [0] * max_len
            for i in range(max_len):
                cur_state[i] = arr[cur] * (i + 1)
            dp[parent[cur]].append(cur_state)
            children[parent[cur]] -= 1
            if children[parent[cur]] == 0:
                leaves.append(parent[cur])
        else:
            cur_state = [0] * max_len
            for exclude in range(max_len):
                sumi = (exclude + 1) * arr[cur]
                for child_state in dp[cur]:
                    sumi += find_min_excluding(child_state, exclude)
                cur_state[exclude] = sumi
            dp[parent[cur]].append(cur_state)
            children[parent[cur]] -= 1
            if children[parent[cur]] == 0:
                leaves.append(parent[cur])
    # print(dp)
    # print(abs(max(dp[0][0][0], dp[0][0][1])) + sum(arr))
    print(min(dp[0][0]))
    return min(dp[0][0])


def check():
    n = 100
    for i in range(100):
        tree = make_graph(n)
        for j in range(100):
            arr = [0] + [randint(1, 15) for i in range(n)]
            temp_brute = brute(n, arr[:], deepcopy(tree))
            temp_solve = solve(n, arr, deepcopy(tree))
            if temp_brute != temp_solve :
                print("Found")
                print(*arr)
                print(tree)
                print("brute", temp_brute)
                print("solve", temp_solve)
                solve(n, arr, deepcopy(tree))
                return
    # print(tree)
    # print(brute(n, arr, tree))

check()

# n = int(input())
# arr = [0] + list(map(int, input().split()))

# tree = defaultdict(lambda: [])

# for i in range(n-1):
#     a, b = map(int, input().split())
#     tree[a].append(b)
#     tree[b].append(a)
# print(brute(n, arr, tree))

