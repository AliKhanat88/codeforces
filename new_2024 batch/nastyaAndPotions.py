import sys

input = sys.stdin.readline

from collections import defaultdict

def solve():
    n, k = map(int, input().split())

    c = [0] + list(map(int, input().split()))


    u_p = list(map(int, input().split()))

    graph_parent = defaultdict(lambda: [])

    graph_children = defaultdict(lambda:[])


    for i in range(n):
        temp = list(map(int, input().split()))
        for j in range(temp[0]):
            graph_children[i+1].append(temp[j+1])
            graph_parent[temp[j+1]].append(i+1)

    rem_children = defaultdict(lambda:0)
    stack = []

    for i in range(1, n+1):
        rem_children[i] = len(graph_children[i])
        if len(graph_children[i]) == 0:
            stack.append(i)
    
    for num in u_p:
        stack.append(num)
        rem_children[num] = 0
        c[num] = 0


    # print("TEST")
    # print(graph_children)
    # print(graph_parent)
    # print(rem_children)

    visited = [False] * (n+1)

    while len(stack) != 0:
        # print(stack)
        # print(c)
        cur = stack.pop()
        if visited[cur] == False:
            visited[cur] = True
            if len(graph_children[cur]) > 0:
                sumi = 0
                for child in graph_children[cur]:
                    sumi += c[child]
                c[cur] = min(c[cur], sumi)

            for parent in graph_parent[cur]:
                rem_children[parent] -= 1
                if rem_children[parent] == 0:
                    stack.append(parent)
    
    print(*c[1:])

for t in range(int(input())):
    solve()