import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    prefix = [0] * (2*n+1)
    arr = [0] * n
    counter = [0] * (2*n+1)
    for i in range(n):
        arr[i] = list(map(int, input().split()))
        if arr[i][0] == arr[i][1]:
            prefix[arr[i][0]] = 1
            counter[arr[i][0]] +=1
    
    for i in range(1, 2*n+1):
        prefix[i] = prefix[i-1] + prefix[i]
    ans = []
    # print(prefix)
    for i in range(1, n+1):
        if prefix[arr[i-1][1]] - prefix[arr[i-1][0] - 1] <= arr[i-1][1] - arr[i-1][0]:
            ans.append("1")
        else:
            if arr[i-1][1] == arr[i-1][0] and counter[arr[i-1][1]] == 1:
                ans.append("1")
            else:
                ans.append("0")
    print("".join(ans))

    


    
for t in range(int(input())):
    solve()