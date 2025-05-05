import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.insert(0, 0)
    tree = [[] for i in range(n+1)]
    for i in range(n-1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
    
    top_sort_tree = [0] * (n+1)
    index = 1
    visited = [False] * (n+1)
    queue = [(1, 0)]

    while len(queue) != 0:    
        new_queue = []
        for i in range(len(queue)):
            for child in tree[queue[i][0]]:
                visited[queue[i][0]] = True
                if not visited[child]:
                    new_queue.append((child, index))
            top_sort_tree[index] = (queue[i][0], queue[i][1])
            index += 1
        queue = new_queue
    
    # print(tree)
    # print(arr)
    # print(top_sort_tree)

    dp = [[] for i in range(n+1)]
    dpi = [0] * (n+1)
    temp_ans = [0 for i in range(20)]
    for i in range(n, 1, -1):
        if len(dp[i]) == 0:
            sumi = 1
        else:
            sumi = sum(dp[i]) + 1
        dpi[top_sort_tree[i][0]] = i
        dp[top_sort_tree[i][1]].append(sumi)
        for b in range(20):
            if (2 ** b) & arr[top_sort_tree[i][0]] != (2 ** b) & arr[top_sort_tree[top_sort_tree[i][1]][0]]:
                temp_ans[b] += sumi
    # print(temp_ans) 
    # print(dp)
    # print(dpi)

    ans = [[0 for i in range(20)] for i in range(n+1)]
    ans[1] = temp_ans
    queue = []
    for child in tree[1]:
        queue.append((child, 1, ans[1][:]))
    
    visited = [False] * (n+1)
    visited[1] = True
    while len(queue) != 0:
        new_queue = []
        for cur in queue:
            visited[cur[0]] = True
            new_temp = [0 for i in range(20)]
            for b in range(20):
                if (2 ** b) & arr[cur[0]] != (2 ** b) & arr[cur[1]]:
                    new_temp[b] = cur[2][b] + n - 2 * (sum(dp[dpi[cur[0]]]) + 1)
                else:
                    new_temp[b] = cur[2][b]
            ans[cur[0]] = new_temp
            for child in tree[cur[0]]:
                if not visited[child]:
                    new_queue.append((child, cur[0], new_temp[:]))
        queue = new_queue
    
    for i in range(1, n+1):
        sumi = 0
        for b in range(20):
            sumi += (2 ** b * ans[i][b])
        print(sumi, end=" ")
    print()
            
            
for t in range(int(input())):
    solve()