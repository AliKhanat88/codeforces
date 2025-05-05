def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 1
    per_nodes = 1
    temp_nodes = 0
    # print("TEST")
    # print(arr)
    for i in range(1, n):
        if arr[i] < arr[i-1] and per_nodes == 1:
            ans += 1
            per_nodes = temp_nodes
            temp_nodes = 1
        elif arr[i] < arr[i-1] and per_nodes != 1:
            per_nodes -= 1
            temp_nodes += 1
        else:
            temp_nodes += 1
        # print(i, per_nodes, temp_nodes)
    print(ans)
for t in range(int(input())):
    solve()


