from bisect import bisect_left

def solve():
    n, m, q = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    queries = list(map(int, input().split()))

    for i in range(q):
        temp = bisect_left(arr, queries[i])
        # print(temp, "index")
        if temp == 0:
            print(arr[0] - 1)
        elif temp == m:
            print(n - arr[-1])
        else:
            print((arr[temp] - arr[temp-1]) // 2)

for t in range(int(input())):
    solve()