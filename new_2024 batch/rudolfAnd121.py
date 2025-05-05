def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    # print("TEST")
    # print(arr)
    for i in range(1, n-1):
        temp = arr[i-1]
        arr[i-1] = 0
        if arr[i] < temp * 2:
            print("NO")
            return
        if arr[i+1] < temp:
            print("NO")
            return
        arr[i] = arr[i] - temp*2
        arr[i+1] = arr[i+1] - temp
        # print(arr)
    for num in arr:
        if num != 0:
            print("NO")
            return
    print("YES")
for t in range(int(input())):
    solve()