def solve():
    n = int(input())
    parent = [0, 0] + list(map(int, input().split()))

    graph = [[] for i in range(n+1)]
    for i in range(2, n+1):
        graph[parent[i]].append(i)

    # print(graph)
    top = 1
    top_sort_tree = [0] * (n+1)
    index = 1
    visited = [False] * (n+1)
    queue = [(top, 0)]

    while len(queue) != 0:
        new_queue = []
        for i in range(len(queue)):
            for child in graph[queue[i][0]]:
                visited[queue[i][0]] = True
                if not visited[child]:
                    new_queue.append((child, index))
            top_sort_tree[index] = queue[i][1]
            index += 1
        queue = new_queue

    # print(top_sort_tree)
    # print(graph)
    dp = [[] for i in range(n+1)]
    # max, count, total count
    ans = 0
    for i in range(n, 0, -1):
        if len(dp[i]) == 0:
            dp[top_sort_tree[i]].append(1)
        elif len(dp[i]) == 1:
            dp[top_sort_tree[i]].append(dp[i][0] + 1)
        else:
            total = sum(dp[i])
            sumi_arr = [-1] * (total + 1)
            sumi_arr[0] = 1
            temp_ans = 0
            for j in range(len(dp[i])):
                new_sumi_arr = [-1] * (total + 1)
                new_sumi_arr[0] = 1
                for k in range(len(sumi_arr)):
                    if k - dp[i][j] >= 0 and sumi_arr[k - dp[i][j]] == 1:
                        new_sumi_arr[k] = 1
                        temp_ans = max(temp_ans, k * (total - k))
                    elif sumi_arr[k] == 1:
                        new_sumi_arr[k] = 1
                sumi_arr = new_sumi_arr
            ans += temp_ans
            # print(sumi_arr, i)
            dp[top_sort_tree[i]].append(total + 1)
    # print(dp)
    print(ans)
                


    

solve()