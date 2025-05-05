def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    temp_arr = [0] * (n+2)
    temp_arr[arr[0]] = 1
    for i in range(1,n):
        if temp_arr[arr[i]-1] != 1 and temp_arr[arr[i]+1] != 1:
            print("NO")
            return
        temp_arr[arr[i]] = 1
    print("YES")


for t in range(int(input())):
    solve()