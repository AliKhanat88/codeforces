def solve():
    n = int(input())
    arr = input().split()
    arr = [(i, int(arr[i])) for i in range(n)]
    arr.sort(key=lambda x: x[1])
    if n == 1:
        print(1)
        return
    sumi_for = [0] * n
    for i in range(1, n):
        sumi_for[i] = sumi_for[i-1] + (arr[i][1] - arr[i-1][1]) * (i)
    
    sumi_back = [0] * n
    for i in range(n-2, -1, -1):
        sumi_back[i] = sumi_back[i+1] + (arr[i+1][1] - arr[i][1]) * (n-i-1)

    print_arr = [0] * n
    for i in range(n):
        print_arr[arr[i][0]] = f"{n + sumi_back[i] + sumi_for[i]}"
    print(" ".join(print_arr))







for t in range(int(input())):
    solve()