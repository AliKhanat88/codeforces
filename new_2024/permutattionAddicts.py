def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    edge = [[] for i in range(n+3)]
    seti = set(arr)
    k = 0
    for i in range(n):
        if arr[i] > i+1:
            k += 1
        edge[arr[i]].append(i+1)
    
    print(k)
    ans = []
    if n+1 in arr:
        initial = n+1
    else:
        initial = 0

    while len(ans) < n:
        for num in edge[initial]:
            if num in seti:
                initial = num
            else:
                ans.append(num)
        ans.append(initial)
    print(*ans[:n])

for t in range(int(input())):
    solve()
