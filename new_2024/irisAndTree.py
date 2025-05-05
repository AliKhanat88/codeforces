import sys
input = sys.stdin.readline

def solve():
    n, w = map(int, input().split())

    parent = list(map(int, input().split()))

    tree = [[] for i in range(n+1)]

    for i in range(2, n+1):
        tree[parent[i-2]].append(i)
    
    for i in range(1, n+1):
        tree[i].sort()
    dfs = [(1, 0)]
    idx = [0] * (n+1)
    cur_path = []
    paths_rev = [[] for i in range(n+1)]
    paths_len = [0] * (n + 1)
    timer = 0
    goal = 2
    # print(tree)
    while dfs:
        v, p = dfs.pop()
        if v > 0:
            if idx[v] >= len(tree[v]):
                continue
            if tree[v][idx[v]] == goal:
                cur_path.append(goal)
                paths_len[timer] = len(cur_path)
                while cur_path:
                    paths_rev[cur_path.pop()].append(timer)
                timer += 1
                if goal + 1 > n:
                    goal = (goal +1) % (n + 1) + 1
                else:
                    goal = goal + 1
            else:
                cur_path.append(tree[v][idx[v]])
            dfs.append((v, p))
            dfs.append((-v, tree[v][idx[v]]))
            dfs.append((tree[v][idx[v]], v))
            idx[v] += 1
        else:
            v, c = -v, p
            if v == goal:
                cur_path.append(c)
                paths_len[timer] = len(cur_path)
                while cur_path:
                    paths_rev[cur_path.pop()].append(timer)
                timer += 1
                if goal + 1 > n:
                    goal = (goal +1) % (n + 1) + 1
                else:
                    goal = goal + 1
                goal = (goal + 1) % (n)
            else:
                cur_path.append(c)
        # print(dfs)
        # print(cur_path)
    # print(paths_rev)
    # print(paths_len)
    
    cur_ans = w * n
    c_w = w
    count = n
    for i in range(n-1):
        ei, wi = map(int, input().split())
        c_w = c_w - wi
        cur_ans = cur_ans - (count - len(paths_rev[ei])) * wi
        for path in paths_rev[ei]:
            paths_len[path] -= 1
            if paths_len[path] == 0:
                count -= 1
                cur_ans -= c_w
        print(cur_ans, end=" ")
            
    print()



            


for t in range(int(input())):
    solve()