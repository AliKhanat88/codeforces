def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    arr = [(arr[i] % k, arr[i]) for i in range(n)]
    arr.sort(key = lambda x: (x[0], -x[1]))
    
    # print(arr)
    odd = 0
    odd_rem = None
    ans = 0
    i = 1
    while i < n:
        if arr[i][0] != arr[i-1][0]:
            odd += 1
            odd_rem = arr[i-1][0]
            i += 1
        else:
            ans += (arr[i-1][1] - arr[i][1]) // k
            i += 2
    
    if i != n+1:
        odd += 1
        odd_rem = arr[-1][0]
    # print(odd)
    if odd > 1:
        print(-1)
        return
    if odd == 0:
        print(ans)
        return
    temp = []
    # print(odd_rem)
    for i in range(n):
        if arr[i][0] == odd_rem:
            temp.append(arr[i])
    if len(temp) == 1:
        print(ans)
        return
    # print(temp)
    before = [0] * (len(temp))
    after = [0] * (len(temp))
    per = 0
    for i in range(1, len(temp), 2):
        before[i-1] = per
        per += (temp[i-1][1] - temp[i][1]) // k
        before[i] = per

    per = 0
    for i in range(len(temp)-2, -1, -2):
        after[i+1] = per
        per += (temp[i][1] - temp[i+1][1]) // k
        after[i] = per
    # print(before, after)
    mini_ans = min(before[-2], after[1])
    for i in range(2, len(temp)-2, 2):
        mini_ans = min(mini_ans, before[i-1]+after[i+1])

    print(ans - before[-2] + mini_ans)
        

for t in range(int(input())):
    solve()