def solve():
    n = int(input())

    arr = list(map(int, input().split()))
    arr.sort()
    first = None
    second = None
    for i in range(1, n):
        if arr[i] == arr[i-1]:
            first = arr[i]
            second = arr[i-1]
    if first == None:
        print(-1)
        return

    arr.remove(first)
    arr.remove(first)
    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i] - 2 * first:
            print(first, first, arr[i], arr[i-1])
            return

    print(-1)
        
for t in range(int(input())):
    solve()