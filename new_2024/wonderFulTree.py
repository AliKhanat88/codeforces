import sys
input = sys.stdin.readline
from collections import deque

def solve():
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    parent = list(map(int, input().split()))

    adj = [[] for i in range(n + 1)]
    for i in range(2, n+1):
        adj[parent[i-2]].append(i)

    # print(adj)
    dfs = [(1, 0)]
    for v, p in dfs:
        for child in adj[v]:
            dfs.append((child, v))
    # print(dfs)
    
    def get_sum(v):
        sumi = 0
        for child in adj[v]:
            sumi += arr[child]
        return sumi
    
    ans = 0
    for v, p in dfs[::-1]:
        if len(adj[v]) == 0:
            continue
        else:
            sumi = get_sum(v)
            if sumi < arr[v]:
                done = [v]
                goal = arr[v] - sumi
                bfs = deque()
                for child in adj[v]:
                    bfs.append((child, 1))
                while goal > 0:
                    cur_v, cur_l = bfs.popleft()
                    if len(adj[cur_v]) == 0:
                        arr[cur_v] += goal
                        ans += (cur_l * goal)
                        goal = 0
                    else:
                        
                        can = get_sum(cur_v) - arr[cur_v]
                        if can >= goal:
                            arr[cur_v] += goal
                            ans += (cur_l * goal)
                            goal = 0
                        else:
                            done.append(cur_v)
                            arr[cur_v] += can
                            ans += (can * cur_l)
                            goal -= can
                        for child in adj[cur_v]:
                            bfs.append((child, cur_l + 1))
                for num in done[::-1]:
                    arr[num] = get_sum(num)
            # print(arr, v)
    # print(arr)
    print(ans)
                    
                
            



for t in range(int(input())):
    solve()