from math import ceil
def solve():
    n = int(input())
    arr = [*map(int, input().split())]
    arr.sort()
    
    i = 0
    j = n - 1
    sumi = 0
    ans = 0
    big = arr[j]

    while i < j:
        sumi += arr[i]
        if sumi >= big:
            ans += big + 1
            sumi = sumi - big
            big = 0
            j -= 1
            if i < j:
                big = arr[j]
        i += 1
    # print(arr)
    # print(i, j , sumi, big)
    if big +sumi == 1:
        ans += 1
    elif big +sumi > 1:
        ans += ceil((big + sumi) / 2) + 1
    print(ans)
for t in range(int(input())):
    solve()