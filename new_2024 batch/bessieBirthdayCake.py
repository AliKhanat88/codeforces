from heapq import heappush, heappop

def solve():
    n, x, y = map(int, input().split())

    arr = list(map(int, input().split()))

    arr.sort()

    heapi1 = []
    heapi2 = []
    ans = 0
    for i in range(1, x):
        if arr[i] - arr[i-1] <= 2:
            ans += arr[i] - arr[i-1]
        elif arr[i] - arr[i-1] > ((arr[i] - arr[i-1] - 1) // 2) * 2 + 1:
            heappush(heapi1, ((arr[i] - arr[i-1] - 1) // 2, -(arr[i] - arr[i-1])))
        else:
            heappush(heapi2, ((arr[i] - arr[i-1] - 1) // 2, -(arr[i] - arr[i-1])))

    if (n - arr[-1] + arr[0]) <= 2:
        ans += (n - arr[-1] + arr[0])
    elif n - arr[-1] + arr[0] > ((n - arr[-1] + arr[0] - 1) // 2) * 2 + 1:
        heappush(heapi1, ((n - arr[-1] + arr[0] - 1) // 2, -(n - arr[-1] + arr[0])))
    else:
        heappush(heapi2, ((n - arr[-1] + arr[0] - 1) // 2, -(n - arr[-1] + arr[0])))
    # print(arr)
    # print(heapi)
    while len(heapi1) != 0:
        temp = heappop(heapi1)
        if abs(temp[0]) <= y:
            ans += (-temp[1])
            y = y - temp[0]
        else:
            ans += (y * 2 + 1)
            y = 0

    while len(heapi2) != 0:
        temp = heappop(heapi2)
        if abs(temp[0]) <= y:
            ans += (-temp[1])
            y = y - temp[0]
        else:
            ans += (y * 2 + 1)
            y = 0
    print(ans-2)
for t in range(int(input())):
    solve()