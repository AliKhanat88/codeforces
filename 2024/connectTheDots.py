import sys
input = sys.stdin.readline
from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    arr = [0] * m
    for i in range(m):
        a, d, k = map(int, input().split())
        arr[i] = [a, d, k]
    arr.sort(key= lambda x: (x[1], x[0] % x[1], x[0]))

    # print(arr)

    per_d = arr[0][1]
    per_m = arr[0][0] % arr[0][1]
    dict_num = defaultdict(lambda:-1)
    per_num = 0
    numb = 1
    graph = defaultdict(lambda: set())
    i = 0
    while i < m:
        if per_d == arr[i][1] and per_m == arr[i][0] % arr[i][1]:
            if arr[i][0] > per_num:
                temp = arr[i][0]
                numb += 1
            else:
                temp = per_num + d
            while temp <= arr[i][0] + arr[i][1] * arr[i][2]:
                if dict_num[temp] == numb:
                    pass
                elif dict_num[temp] == -1:
                    dict_num[temp] = numb
                else:
                    graph[numb].add(dict_num[temp])
                    graph[dict_num[temp]].add(numb)
                temp = temp + arr[i][1]
            per_num = temp - d
        else:
            per_d = arr[i][1]
            per_m = arr[i][0] % arr[i][1]
            per_num = 0
            i -= 1
            numb += 1
        i += 1
    # print(dict_conn)
    # print(dict_num)
    # print(graph)
    # print(dict_num)
    ans = 0
    visited = set()
    for i in range(1, n+1):
        if dict_num[i] == -1:
            ans += 1
        elif dict_num[i] in visited:
            pass
        else:
            stack = [dict_num[i]]
            while len(stack) != 0:
                cur = stack.pop()
                if cur not in visited:
                    visited.add(cur)
                    for child in graph[cur]:
                        if child not in visited:
                            stack.append(child)
            ans += 1
    print(ans)
for t in range(int(input())):
    solve()