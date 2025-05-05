from heapq import heappop, heappush

def solve():
    n, m = map(int, input().split())
    forw_adj = [set() for i in range(n+1)]
    back_adj = [set() for i in range(n+1)]

    for i in range(m):
        a, b = map(int, input().split())
        forw_adj[a].add(b)
        back_adj[b].add(a)
    
    forword = [0] * (n + 1)
    backword = [0] * (n + 1)
    heap = []
    visited = [False] * (n + 1)
    for i in range(1, n + 1):
        forword[i] = len(forw_adj[i])
        backword[i] = len(back_adj[i])
        heappush(heap, (-(forword[i] - backword[i]), i))
    ans = []
    # print(forw_adj)
    # print(back_adj)
    # print(heap)
    while heap:
        diff, index = heappop(heap)
        if not visited[index] and -(forword[index] - backword[index]) == diff:
            ans.append(index)
            visited[index] = True
            for num in forw_adj[index]:
                if not visited[num]:
                    back_adj[num].remove(index)
                    backword[num] -= 1
                    heappush(heap, (-(forword[num] - backword[num]), num))
            for num in back_adj[index]:
                if not visited[num]:
                    forw_adj[num].remove(index)
                    forword[num] -= 1
                    heappush(heap, (-(forword[num] - backword[num]), num))
            # print(index)
            # print(forword)
            # print(backword)
    print(*ans)



for t in range(int(input())):
    solve()