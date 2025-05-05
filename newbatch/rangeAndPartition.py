

def solve():
    n, k = map(int, input().split())

    arr = list(map(int, input().split()))

    count_prefix = [0] * (n+1)

    for i in range(len(arr)):
        count_prefix[arr[i]] += 1
    
    for i in range(1, n+1):
        count_prefix[i] = count_prefix[i-1] + count_prefix[i]

    # print(count_prefix)
    # print(arr)
    if (n - k) % 2 == 1:
        target = k + (n - k) // 2 + 1
    else:
        target = k + (n - k) // 2
    mini = float("inf")
    mini_move = None
    for i in range(1, n+1):
        lower = i
        upper = n
        while lower + 1 < upper:
            mid = lower + (upper - lower) // 2
            if count_prefix[mid] - count_prefix[i-1] >= target:
                upper = mid
            else:
                lower = mid + 1
        if count_prefix[lower] - count_prefix[i-1] >= target:
            if lower - i < mini:
                mini = lower - i
                mini_move = (i, lower)
        if count_prefix[upper] - count_prefix[i-1] >= target:
            if upper - i < mini:
                mini = upper - i
                mini_move = (i, upper)
        
    print(*mini_move)

    did = 0
    outi = 0
    ini = 0
    per = 0
    for i in range(n):
        if did >= k-1:
            break
        if arr[i] >= mini_move[0] and arr[i] <= mini_move[1]:
            ini += 1
        else:
            outi += 1
        if ini > outi:
            print(per+1, i+1)
            per = i + 1
            outi = 0
            ini = 0
            did += 1
    print(per+1, n)           
for t in range(int(input())):
    solve()