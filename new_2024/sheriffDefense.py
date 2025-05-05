from collections import defaultdict

def solve():
    n, c = map(int, input().split())

    arr = [0] + list(map(int, input().split()))
    
    tree = defaultdict(lambda: [])
    for i in range(n-1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
    
    children = [0] * (n + 1)
    parent = [-1] * (n + 1)
    dp = defaultdict(lambda: [])
    stack = [(1, 0)]
    visited = [False] * (n+1)
    leaves = []
    while stack:
        new_stack = []
        for num in stack:
            visited[num[0]] = True
            parent[num[0]] = num[1]
            for child in tree[num[0]]:
                if not visited[child]:
                    new_stack.append((child, num[0]))
                    children[num[0]] += 1
            if children[num[0]] == 0:
                leaves.append(num[0])
        stack = new_stack
    # print(leaves)
    # print(children)
    # print(parent)
    while leaves:
        cur = leaves.pop()
        children[parent[cur]] -= 1
        if children[parent[cur]] == 0:
            leaves.append(parent[cur])
        dp[cur].sort(reverse=True)
        sumi = 0
        not_have = 0
        for num in dp[cur]:
            sumi += num[1]
            not_have += max(num)
        
        have = arr[cur] + sumi
        cur_sum = 0
        count = 0
        for i in range(len(dp[cur])):
            sumi -= dp[cur][i][1]
            if dp[cur][i][1] + 2 * c >= dp[cur][i][0]:
                cur_sum += dp[cur][i][1]
            else:
                cur_sum += dp[cur][i][0]
                count += 1
            have = max(have, arr[cur] + cur_sum - count * 2 * c + sumi)
        dp[parent[cur]].append((have, not_have))
        # print(cur, have, not_have)
        if cur == 1:
            break
    print(max(dp[0][0][1], dp[0][0][0]))
    # print(dp)


for t in range(int(input())):
    solve()