import sys
input = sys.stdin.readline
mod = 998244353
n = int(input())
graph = [[] for i in range(n + 1)]
children = [0] * (n + 1)
parents = [[] for i in range(n+1)]
counts = [[0 for i in range(3)] for j in range(n+1)]
stack = []
for i in range(1, n+1):
    k = int(input())
    if k == 0:
        stack.append(i)
    for j in range(k):
        a, b = map(int, input().split())
        graph[i].append((a, b))
        parents[a].append((i, b))
    
# print(graph)
# print(parents)
# print(stack)
while len(stack) != 0:
    # print(stack)
    cur = stack.pop()
    cur0 = 0
    cur1 = 0
    for child in graph[cur]:
        temp0 = counts[child[0]][0]
        temp1 = counts[child[0]][1]
        if child[1] == 1:
            temp1 += 1
        else:
            temp0 += 1
        counts[cur][2] += (cur1 * temp0)
        counts[cur][2] = counts[cur][2] % mod
        cur0 = (cur +  temp0) % mod
        cur1 = (cur1 + temp1) % mod
    for par in parents[cur]:
        if par[1] == 1:
            counts[par[0]][2] += counts[cur][0]
            counts[par[0]][1] += 1
        else:
            counts[par[0]][0] += 1
        counts[par[0]][0] += counts[cur][0]
        counts[par[0]][1] += counts[cur][1]
        counts[par[0]][2] += (counts[cur][2])
        counts[par[0]][0] %= mod
        counts[par[0]][1] %= mod
        counts[par[0]][2] %= mod
        children[par[0]] += 1
        if children[par[0]] >= len(graph[par[0]]):
            stack.append(par[0])
# ans = counts[1][2]
# # print(ans)
# cur0 = 0
# cur1 = 0
# for child in graph[1]:
#     counts[child[0]][child[1]] += 1
#     ans += cur1 * counts[child[0]][0]
#     cur0 += counts[child[0]][0]
#     cur1 += counts[child[0]][1]
#     ans = ans % mod
# print(counts)
print(counts[1][2] % mod)