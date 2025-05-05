from collections import defaultdict

inf = float("inf")
def solve():
    n, m = map(int, input().split())
    graph = defaultdict(lambda: [])

    for i in range(m):
        a, b, w = map(int, input().split())
        graph[a].append([b, w])
        graph[b].append([a, w])


    bit = ["0"] * n
    bit[0] = "1"
    cur_edges = []
    visited = set()
    for child in graph[1]:
        cur_edges.append(child)
    # print(graph)
    visited.add(1)
    done = False
    ans = []
    sumi = 0
    br = False
    for i in range(n * n + 1):
        # print(cur_edges)
        if len(cur_edges) == 0:
            break
        mini = inf
        for j, num in enumerate(cur_edges):
            mini = min(mini, num[1])
        sumi += mini
        ans.append(f"{''.join(bit)} {mini}")
        # print(mini)
        j = 0
        new_edges = []
        while j < len(cur_edges):
            if cur_edges[j][0] == n:
                done = True
            if cur_edges[j][1] == mini:
                # print("YES")
                temp = cur_edges[j]
                bit[temp[0] - 1] = "1"
                visited.add(temp[0])
                for child in graph[temp[0]]:
                    # print(child)
                    if child[0] not in visited:
                        new_edges.append(child)
                # print(temp, n)
                if temp[0] == n:
                    br = True
                    break
            else:
                new_edges.append([cur_edges[j][0], cur_edges[j][1] - mini])
            j += 1
        if br:
            break
        cur_edges = new_edges


    if done == False:
        print("inf")
        return
    print(sumi, len(ans))
    print("\n".join(ans))



solve()