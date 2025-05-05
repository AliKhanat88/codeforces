import sys
input = sys.stdin.readline

from collections import defaultdict

def solve():
    n = int(input())
    tree = defaultdict(lambda: [])
    for i in range(n-1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
    parent = [-1] * (n + 1)
    visited = [False] * (n + 1)
    stack = [(1, 0)]
    real_children = defaultdict(lambda: 0)

    while len(stack):
        newstack = []
        for num in stack:
            if not visited[num[0]]:
                parent[num[0]] = num[1]
                visited[num[0]] = True
                c = 0
                for child in tree[num[0]]:
                    if not visited[child]:
                        newstack.append((child, num[0]))
                        c += 1
                real_children[num[0]] = c
                    

        stack = newstack

    # print(parent)
    visited = [False] * (n + 1)

    count = 0
    minus = 0

    stack = [1]
    exclude = []
    mini = float("inf")
    while len(stack):
        newstack = []
        for num in stack:
            if not visited[num]:
                count += 1
                visited[num] = True
                temp_a = 0
                for child in tree[num]:
                    if not visited[child]:
                        newstack.append(child)
                        temp_a += 1
                if temp_a == 0:
                    exclude.append(num)
        mini = min(mini, n - count + minus)
        # print(exclude)
        while len(exclude):
            cur = exclude.pop()
            minus += 1
            real_children[parent[cur]] -= 1
            if real_children[parent[cur]] <= 0 and real_children[parent[cur]] != -1:
                exclude.append(parent[cur])
            


        stack = newstack
    print(mini)




for t in range(int(input())):
    solve()