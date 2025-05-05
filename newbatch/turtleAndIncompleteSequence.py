def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    cur_list = [[] for i in range(n+1)]
    last = None
    for i in range(n):
        if arr[i] != -1:
            if last == None:
                last = i
            else:
                if arr[i] >= arr[last]:
                    a, b = arr[i], arr[last]
                else:
                    b, a = arr[i], arr[last]

                queue = [b]
                temp = last
                while len(queue) != 0:
                    if temp >= i:
                        break
                    new_queue = []
                    for node in queue:
                        # Dequeue a node from the front of the queue
                        # node = queue.pop(0)
                        
                        if node >= 1 and node <= 10 ** 9 and a % node == 0:
                            new_queue.append(node * 2)
                            new_queue.append(node * 2 + 1)
                            new_queue.append(node // 2)
                        else:
                            new_queue.append(node // 2)
                    queue = new_queue
                    print(queue)
                    temp = temp+1
                if len(queue) == 0 or a not in queue:
                    print(-1)
                    return
    print("done")
for t in range(int(input())):
    solve()