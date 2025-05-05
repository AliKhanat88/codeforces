import sys
input = sys.stdin.readline

def solve(n , m, graph):
    # print(graph)
    ans = [set(), set()]
    visited = [False] * (n + 1)
    stack = [(1, 0, -1)]
    alice_win = False
    while stack and not alice_win:
        num = stack.pop()
        visited[num[0]] = True
        ans[num[1]].add(num[0])
        for child in graph[num[0]]:
            if child != num[2]:
                if visited[child]:
                    if child in ans[num[1]]:
                        alice_win = True
                        break
                else:
                   stack.append((child, (num[1] + 1) % 2, num[0]))
            if alice_win:
                break
    # if alice_win:
    #     print("Alice")
    #     return "Alice"
    # else:
    #     print("Bob")
    #     return "Bob"
    # print(alice_win)
    if alice_win:
        print("Alice", flush=True)
        sys.stdout.flush()
        for i in range(n):
            print(1, 2, flush=True)
            sys.stdout.flush()
            if input().strip() == "-1":
                quit()
    else:
        print("Bob", flush=True)
        sys.stdout.flush()
        # print(ans)
        ans[0] = list(ans[0])
        ans[1] = list(ans[1])
        if len(ans[0]) + len(ans[1]) != n:
            raise Exception()
        for i in range(n):
            colors = input().strip()
            if colors == "-1":
                quit()
            colors = list(map(int, colors.split()))
            if len(ans[0]) == 0:
                temp = ans[1].pop()
                if 2 in colors:
                    print(temp, 2, flush=True)
                elif 3 in colors:
                    print(temp, 3, flush=True)
                sys.stdout.flush()
                continue
            if len(ans[1]) == 0:
                temp = ans[0].pop()
                if 1 in colors:
                    print(temp, 1, flush=True)
                elif 3 in colors:
                    print(temp, 3, flush=True)
                sys.stdout.flush()
                continue
            if 1 in colors:
                temp = ans[0].pop()
                print(temp, 1, flush=True)
                sys.stdout.flush()
                continue
            if 2 in colors:
                temp = ans[1].pop()
                print(temp, 2, flush=True)
                sys.stdout.flush()
                continue
        
        



def main():
    for t in range(int(input())):
        temp = input()
        if temp == "-1":
            quit()
        n, m = map(int, temp.split())
        graph = [[] for i in range(n + 1)]
        for i in range(m):
            a,b = map(int, input().split())
            graph[a].append(b)
            graph[b].append(a)
        solve(n, m, graph)

main()
def brute_force(n, m, adj):
    bfs = [0]
    bip = [-1]*n
    bip[0] = 0
    i=0
    happy=True
    sides=[[0],[]]
    while i<len(bfs):
        u = bfs[i]
        d = bip[u]
        for v in adj[u]:
            if bip[v]==d:
                happy=False
                break
            elif bip[v]==-1:
                bip[v]=1-d
                sides[1-d].append(v)
                bfs.append(v)
        if not happy:break
        i+=1
    
    if happy:
        return "Bob"
    else:
        return "Alice"



import random
def generate_connected_graph(n, m):
    if m < n - 1:
        raise ValueError("The number of edges m must be at least n-1 to ensure connectivity.")

    edges = set()
    
    # Step 1: Create a spanning tree to ensure connectivity
    for i in range(2, n + 1):
        # Connect each node i with a random previous node (1 through i-1)
        u = random.randint(1, i - 1)
        edges.add((u, i))

    # Step 2: Add additional random edges until we reach exactly m edges
    while len(edges) < m:
        u = random.randint(1, n)
        v = random.randint(1, n)
        
        # Avoid self-loops and duplicate edges
        if u != v and (u, v) not in edges and (v, u) not in edges:
            edges.add((u, v))
    
    # Convert edges set to a list and return
    return list(edges)


def checker():
    n = 2
    m = 1
    for i in range(50):
        edges = generate_connected_graph(n ,m)
        graph1 = [[] for i in range(n + 1)]
        graph2 = [[] for i in range(n)]
        for edge in edges:
            graph1[edge[0]].append(edge[1])
            graph1[edge[1]].append(edge[0])
            graph2[edge[0] - 1].append(edge[1] - 1)
            graph2[edge[1] - 1].append(edge[0] - 1)
        if solve(n, m, graph1) != brute_force(n, m, graph2):
            print("Found")
            print(graph1)
            return

# checker()


