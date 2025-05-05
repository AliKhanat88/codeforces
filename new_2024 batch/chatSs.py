def solve():
    n, k = map(int, input().split())
    ans_arr = list(map(int, input().split()))
    if k == 1:
        print("YES")
        return
    if n <= 2:
        print("YES")
        return
    arr2 = list(map(int, input().split()))
    for i in range(1, n):
        if ans_arr[i] == arr2[0] and 


for t in range(int(input())):
    solve()