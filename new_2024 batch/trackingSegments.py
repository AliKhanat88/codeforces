import sys
input = sys.stdin.readline

def check(n, queries,segments, mid):
    arr = [0] * (n+1)
    for i in range(mid+1):
        arr[queries[i]] = 1
    for i in range(1, n+1):
        arr[i] = arr[i-1] + arr[i]
    
    for segment in segments:
        if arr[segment[1]] - arr[segment[0] - 1] > (segment[1] - segment[0] + 1) // 2:
            return True
    return False
def solve():
    n, m = map(int, input().split())
    segments = [0] * m
    for i in range(m):
        segments[i] = tuple(map(int, input().split()))
    q = int(input())
    queries = [0] * q
    for i in range(q):
        queries[i] = int(input())
    # print("test")
    # print(segments)
    # print(queries)
    mini = 0
    maxi = len(queries) - 1
    while maxi > mini:
        mid = mini + (maxi - mini) // 2
        # print(mini, maxi, mid, check(n, queries, segments, mid))
        if check(n, queries, segments, mid):
            maxi = mid
        else:
            mini = mid + 1
    if check(n, queries, segments, mini):
        print(maxi+1)
    else:
        print(-1)

for t in range(int(input())):
    solve()