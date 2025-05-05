import heapq

def find_zero(arr, t):
    val = 0
    for num in arr:
        if num >= -t:
            val += 1
    return val

def solve():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    index_vals = [0] * n
    for num in arr:
        index_vals[num-1] -= 1
    # print(index_vals)
    heapq.heapify(index_vals)
    cur = heapq.heappop(index_vals)
    t = 0
    per = 0
    while -t > cur:
        zeros = find_zero(index_vals, t) - per
        t += 1
        temp = zeros
        while temp != 0:
            if -t <= cur:
                break
            heapq.heappush(index_vals, cur+1)
            cur = heapq.heappop(index_vals)
            temp -= 1
        per = zeros - temp
    if per != 0:
        print(t + 1)
    else:
        print(t)

for t in range(int(input())):
    solve()