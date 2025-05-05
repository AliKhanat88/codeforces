import sys
input = sys.stdin.readline
from collections import defaultdict


def check(n, x, k, children, parent_graph):

    
    counts = [0] * (n+1)
    for i in range(1, n+1):
        if children[i] == 0:
            cur = i
            cur_count = 0
            while cur != -1 and children[cur] < 2:
                # print("---------")
                # print(cur)
                # print(counts)
                # print(children)
                counts[cur] += (cur_count + 1)
                children[cur] -= 1
                cur_count = counts[cur]
                if cur_count >= x and k >= 1:
                    counts[cur] = -1
                    cur_count = 0
                    k -= 1
                cur = parent_graph[cur]
            
            if cur != -1:
                children[cur] -= 1
                counts[cur] += cur_count
    # print(children)
    # print(counts)
    if counts[1] >= x and k <= 0:
        return True
    return False

        
    



def solve():
    n, k = map(int, input().split())

    graph = defaultdict(lambda:set())

    for i in range(n-1):
        a, b = map(int, input().split())
        graph[a].add(b)
        graph[b].add(a)

    # print("TEST")
    # print(graph)

    children = [0] * (n+1)
    parent_graph = [-1] * (n+1)
    # making 1 rooted
    st = [(1, -1)]
    while len(st) != 0:
        cur = st.pop()
        parent_graph[cur[0]] = cur[1]
        count = 0
        for child in graph[cur[0]]:
            if child != cur[1]:
                st.append((child, cur[0]))
                count += 1

        children[cur[0]] = count

    # print(children)
    # print(parent_graph)
    lower = 1
    upper = n // (k+1)
    while upper - lower > 1:
        mid =  lower + (upper - lower) // 2
        if check(n, mid, k, children[:], parent_graph):
            lower = mid
        else:
            upper = mid - 1
    if check(n, upper, k, children[:], parent_graph):
        print(upper)
    else:
        print(lower)
    x = 3
    # print(check(n, x, k, children[:], parent_graph))

for t in range(int(input())):
    solve()

