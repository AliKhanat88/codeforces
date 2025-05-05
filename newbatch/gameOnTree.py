import sys
input =  sys.stdin.readline

def solve():
    n, t = map(int, input().split())
    graph = [[] for i in range(n+1)]

    for i in range(n-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    top = int(input())
    top_sort_tree = [0] * (n+1)
    index = 1
    visited = [False] * (n+1)
    queue = [(top, -1, 0)]

    while len(queue) != 0:
        new_queue = []
        for i in range(len(queue)):
            for child in graph[queue[i][0]]:
                visited[queue[i][0]] = True
                if not visited[child]:
                    new_queue.append((child, index, queue[i][2]+1))
            top_sort_tree[index] = (queue[i][1], queue[i][2])
            index += 1
        queue = new_queue

    # print(graph)
    # print(top_sort_tree)
    ans_arr= [None] * (n+1)

    for i in range(n, 1, -1):
        if ans_arr[i] == None:
            if top_sort_tree[i][1] % 2 == 0:
                ans_arr[i] = False
            else:
                ans_arr[i] = True
        if top_sort_tree[top_sort_tree[i][0]][1] % 2 == 0 and ans_arr[i] == True:
            ans_arr[top_sort_tree[i][0]] = True
        elif top_sort_tree[top_sort_tree[i][0]][1] % 2 == 1 and ans_arr[i] == False:
            ans_arr[top_sort_tree[i][0]] = False
    
    # print(ans_arr)
    if ans_arr[1] == True:
        print("Ron")
    else:
        print("Hermione")
    # print(ans_arr[1])


solve()