import sys
input = sys.stdin.readline

def solve():
    n,m,k = map(int, input().split())

    arr = [0] * k
    for i in range(k):
        a,b = map(int, input().split())
        arr[i] = (b, a, i)
    arr.sort(key=lambda x: (x[0], -x[1]))
    # print(arr)
    ans = 0
    ans_arr = [False] * k
    curx = 1
    cury = 0
    for i in range(k):
        if cury < arr[i][1]:
            temp = (arr[i][0] - curx) * (n - cury)
            if i +1 == k- 1:
                diff = (m - curx+1) * (n - cury)
            else:
                if arr[i+1][0] == arr[i][0]:
                    diff = (arr[i+1][0] - arr[]) * (n - cury)
            ans_arr[arr[i][2]] = 1
            ans += temp
            curx = arr[i][0]
            cury = arr[i][1]
        else:
            ans_arr[arr[i][2]] = 0
    ans += (m - curx+1) * (n - cury)
    print(ans)
    print(*ans_arr)
for t in range(int(input())):
    solve()