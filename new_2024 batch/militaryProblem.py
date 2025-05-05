import sys 
input = sys.stdin.readline
from collections import defaultdict, deque

graph = defaultdict(lambda:[])

n, q = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(2, n+1):
    graph[arr[i-2]].append(i)

# print(arr)
# print(graph)
queue = deque(maxlen=n)
order = [-1] * (n)
i = 0
queue.append((1, 1))
while len(queue) != 0:
    cur = queue.pop()
    order[i] = cur[0]
    i += 1
    graph[cur[0]].sort(reverse=True)
    for num in graph[cur[0]]:
        if num != cur[1]:
            queue.append((num, cur[0]))
#     print(queue)
# print(order)
order_index = [0] * (n+1)
for i, num in enumerate(order):
    order_index[num] = i

decendents = [1] * (n+1)

for i in range(n, 0, -1):
    for num in graph[i]:
        decendents[i] += decendents[num]

# print(decendents)

for i in range(q):
    a, k = map(int, input().split())
    if k > decendents[a]:
        print(-1)
    else:
        print(order[order_index[a]+k-1])
    
