import sys
input = sys.stdin.readline

def query(x, y):
    print("?", x, y, flush=True)
    return int(input())

def solve():
    n, = map(int, input().split())
    arr = list(map(int, input().split()))
    adj = [[] for i in range(n+1)]
    for i in range(n):
        adj[arr[i]].append(i+1)
    first = -1
    second = -1
    for i in range(1, n+1):
        if len(adj[i])>= 1 and first==-1:
            first = i
        elif len(adj[i])>= 1 and second == -1:
            second = i
    if second != -1:
        temp=query(adj[first][0], adj[second][0])
        if temp == 0:
            print("! A", flush=True)
        else:
            print("! B", flush=True)
    else:
        temp1 = query(1, 2)
        temp2 = query(1, 3)
        if temp1 <= 0 and temp2 <= 0:
            print("! A", flush=True)
        else:
            print("! B", flush=True)


for t in range(int(input())):
    solve()