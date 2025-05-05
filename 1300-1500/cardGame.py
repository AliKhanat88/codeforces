def solve():
    n = int(input())
    arr = [*map(int, input().split())]
    if n == 1:
        if arr[0]>0:
            print(arr[0])
        else:
            print(0)
        return
    ans = 0
    sumi = 0
    for i in range(n-1, -1, -1):
        if (i+1) % 2 == 0:
            if arr[i] >0:
                sumi += arr[i]
            else:
                ans += sumi
                sumi = 0
        else:
            if arr[i] >= 0:
                ans += sumi + arr[i]
                sumi = 0
    if sumi > 0:
        if abs(arr[0]) <= arr[1]:
            ans += sumi + arr[0]
        else:
            ans += sumi - arr[1]
    print(ans)
for t in range(int(input())):
    solve()