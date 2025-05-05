from heapq import heapify, heappop, heappush
def solve():
    n = int(input())
    arr = input().split()
    arr = [[-int(arr[i]), i+1] for i in range(n)]

    heapify(arr)
    ans = []
    a = heappop(arr)
    while a[0] != 0:
        b = heappop(arr)
        if b[0] == 0:
            break
        a[0] += 1
        b[0] += 1
        ans.append(f"{a[1]} {b[1]}")
        heappush(arr, a)
        heappush(arr, b)
        a = heappop(arr)
    print(len(ans))
    if len(ans) != 0:
        print("\n".join(ans))


for t in range(int(input())):
    solve()