import sys
input = sys.stdin.readline
from math import log2

def solve():
    n, q = map(int, input().split())
    parent = [-1, -1] + list(map(int, input().split()))
    arr = [-1] + list(map(int, input().split()))
    k = log2(n + 1)
    parent_in_arr = [0] * (n + 1)
    children_in_arr = [[] for i in range(n + 1)] 
    stack = [(0, 1)]
    next = 1
    while len(stack) != 0:
        cur = stack.pop()
        parent_in_arr[next] = cur[0]
        children_in_arr[cur[0]].append(next)
        if cur[1] < k:
            stack.append((next, cur[1] + 1))
            stack.append((next, cur[1] + 1))
        next += 1
    # print(parent_in_arr)
    # print(parent)
    # print(arr)
    # print(children_in_arr)
    trouble = 0
    for i in range(1, n+1):
        if arr[parent_in_arr[i]] != parent[arr[i]]:
            trouble += 1
    # print(trouble)

    for i in range(q):
        a, b = map(int, input().split())
        oper = set()
        oper.add(a)
        for child in children_in_arr[a]:
            oper.add(child)
        oper.add(b)
        for child in children_in_arr[b]:
            oper.add(child)
        for op in oper:
            if parent[arr[op]] != arr[parent_in_arr[op]]:
                trouble -= 1
        arr[a], arr[b] = arr[b], arr[a]
        for op in oper:
            if parent[arr[op]] != arr[parent_in_arr[op]]:
                trouble += 1
        # print(trouble)
        if trouble == 0 and arr[1] == 1:
            print("YES")
        else:
            print("NO")



    

for t in range(int(input())):
    solve()