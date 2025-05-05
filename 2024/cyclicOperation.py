from collections import defaultdict

def solve():
    n, k = map(int,input().split())
    arr = [0] + list(map(int, input().split()))
    if k == 1:
        for i in range(1, n+1):
            if arr[i] != i:
                print("NO")
                return
        print("YES")
        return
    temp = 1
    visited = [0] * (n+1)
    for i in range(1, n + 1):
        if visited[i] == 0:
            dict = defaultdict(lambda: -1)
            num = 1
            cur = i
            while visited[cur] == 0:
                visited[cur] = temp
                dict[cur] = num
                num += 1
                cur = arr[cur]
            if visited[cur] == temp and num - dict[cur] != k:
                print("NO")
                return
            temp += 1
    print("YES")
for t in range(int(input())):
    solve()