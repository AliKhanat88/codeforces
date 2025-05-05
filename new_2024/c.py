def solve():
    n, m, v = map(int, input().split())

    arr = list(map(int, input().split()))


    from_left = [0] * (n + 1)
    from_right = [0] * (n + 1)
    cur = 0
    for i in range(1, n +1):
        cur += arr[i-1]
        if cur >= v:
            cur = 0
            from_left[i] = from_left[i-1] + 1
        else:
            from_left[i] = from_left[i-1]
    
    cur = 0
    for i in range(n-1, -1, -1):
        cur += arr[i]
        if cur >= v:
            cur = 0
            from_right[i] = from_right[i+1] + 1
        else:
            from_right[i] = from_right[i+1]
    if from_left[n] < m:
        print(-1)
        return
    print(from_left)
    print(from_right)
    cur_sum = 0
    per = 0
    ans = 0
    for i in range(n):
        cur_sum += arr[i]
        while from_left[per] + from_right[i+1] < m:
            cur_sum -= arr[per]
            per += 1
        ans = max(ans, cur_sum)
        # print(per, cur_sum)
    print(ans)
        
for t in range(int(input())):
    solve()