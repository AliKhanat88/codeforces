def solve():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    ans = [1] * (n+1)
    ans[1] = 0
    ans[0] = -1
    for i in range(2, n+1):
        for j in range(i+i, n+1, i):
            ans[j] = max(ans[j], ans[i] + 1)
    
    if max(ans) >= m:
        print(-1)
        return
    
    print(*[arr[num] for num in ans[1:]])


for t in range(int(input())):
    solve()