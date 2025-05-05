def solve():
    n, c = map(int, input().split())

    arr = list(map(int, input().split()))

    maxi = [0] * n
    arr[0] += c
    maxi[0] = arr[0]
    sumi_arr = [0] * n
    sumi_arr[0] = arr[0]
    for i in range(1, n):
        maxi[i] = max(maxi[i-1], arr[i])
        sumi_arr[i] = sumi_arr[i-1] + arr[i]

    # print(maxi)
    some_maxi = max(arr)
    ans = []
    if arr[0] >= some_maxi:
        ans.append(0)
    else:
        ans.append(1)

    for i in range(1, n):
        if arr[i] > some_maxi:
            ans.append(0)
        elif arr[i] >= some_maxi:
            if maxi[i-1] >= arr[i]:
                ans.append(i)
            else:
                ans.append(0)
        else:
            if sumi_arr[i] >= some_maxi:
                ans.append(i)
            else:
                ans.append(i+1)
    print(*ans)
        
    
for t in range(int(input())):
    solve()