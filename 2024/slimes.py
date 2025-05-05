inf = 999999999999999999
def check_back(sumi_arr, same, ind, x):
    l = 0
    r = ind - 1
    if l > r:
        return inf
    while l + 1 < r:
        m = (l + r) // 2
        if same[ind-1] == same[m]:
            r = m - 1
        else:
            if sumi_arr[ind] - sumi_arr[m] > x:
                l = m
            else:
                r = m - 1
    # print(l, r)
    if same[ind-1] != same[r] and sumi_arr[ind] - sumi_arr[r] > x:
        return r
    elif same[ind-1] != same[l] and sumi_arr[ind] - sumi_arr[l] > x:
        return l
    else:
        return inf

def check_for(sumi_arr, same, ind, x):
    l = ind + 1
    r = len(same) - 1
    if l > r:
        return inf
    while l + 1 < r:
        m = (l + r) // 2
        if same[ind+1] == same[m]:
            l = m + 1
        else:
            if sumi_arr[m + 1] - sumi_arr[ind+1] > x:
                r = m
            else:
                l = m + 1
    # print(l, r)
    if same[ind+1] != same[l] and sumi_arr[l+1] - sumi_arr[ind+1] > x:
        return l
    elif same[ind+1] != same[r] and sumi_arr[r + 1] - sumi_arr[ind+1] > x:
        return r
    else:
        return inf

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    sumi_arr = [0] * (n + 1)

    for i in range(n):
        sumi_arr[i+1] = sumi_arr[i] + arr[i]

    same = [0] * n
    same[0] = 0
    start = 0
    for i in range(1, n):
        if arr[i] != arr[i-1]:
            start += 1
        same[i] = start
    # print(arr)
    # print(sumi_arr)
    # print(same)

    # print(check_for(sumi_arr, same, 3, 0))
    ans = []
    for i in range(n):
        mini = inf
        if i != 0:
            if arr[i-1] > arr[i]:
                ans.append(1)
                continue
            temp = check_back(sumi_arr, same, i, arr[i])
            if temp != inf:
                mini = min(mini, i - temp)
        if i != n-1:
            if arr[i+1] > arr[i]:
                ans.append(1)
                continue
            temp = check_for(sumi_arr, same, i, arr[i])
            if temp != inf:
                mini = min(mini, temp - i)
        # print(mini, i)
        if mini == inf:
            ans.append(-1)
        else:
            ans.append(mini)
    print(*ans)



    

for t in range(int(input())):
    solve()