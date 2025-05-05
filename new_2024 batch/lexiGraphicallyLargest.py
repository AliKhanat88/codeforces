from collections import defaultdict

def solve():
    n = int(input())
    arr = input().split()
    dict = defaultdict(lambda: -1)
    arr = [(i+1, int(arr[i]) + i+1) for i in range(n)]
    # print(arr)
    for i, num in enumerate(arr):
        dict[num[1]] = i+1
    arr.sort(key=lambda x: x[1])
    # print("TEST")
    # print([num[1] for num in arr])
    # print(arr)

    ans = set()

    last = 999999999999
    for i in range(n-1, -1, -1):
        last = min(last, arr[i][1])
        ans.add(last)
        last -= 1

    print(*sorted(list(ans),reverse=True))




for t in range(int(input())):
    solve()