import sys
input = sys.stdin.readline
inf = 9999999999999999999
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    arr = [0] + arr
    parent = list(map(int, input().split()))
    parent = [0, 0] + parent
    tree = [[] for i in range(n+1)]
    for i in range(2,n+1):
        tree[parent[i]].append(i)
    
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

    dp = [inf for i in range(n+1)]
    for i in range(n, 1, -1):
        if dp[i] == inf:
            dp[i] = arr[top_sort_tree[i][0]]
            dp[top_sort_tree[i][1]] = min(dp[top_sort_tree[i][1]], dp[i])
        else:
            if arr[top_sort_tree[i][0]] <= dp[i]:
                dp[i] = arr[top_sort_tree[i][0]] + (dp[i] - arr[top_sort_tree[i][0]]) // 2
            dp[top_sort_tree[i][1]] = min(dp[top_sort_tree[i][1]], dp[i])
    print(dp[1] + arr[1])


            
for t in range(int(input())):
    solve()