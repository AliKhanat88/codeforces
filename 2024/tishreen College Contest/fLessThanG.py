from math import log2

def check(sumi_arr, x, minus_ind, l, r):
    while l + 1 < r:
        m = (l + r) // 2
        if sumi_arr[m+1] - sumi_arr[minus_ind] < x:
            l = m
        else:
            r = m
    if sumi_arr[r+1] - sumi_arr[minus_ind] < x:
        return r
    else:
        return l
    
inf = 999999999999
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    max_bits = int(log2(10 ** 6))

    last = [[0 for i in range(max_bits+1)] for i in range(n+1)]

    # print(last)
    for b in range(max_bits + 1):
        last[-1][b] = n

    # print(last)
    for b in range(max_bits + 1):
        for i in range(n-1, -1, -1):
            if (2 ** b) & brr[i] != 0:
                last[i][b] = i
            else:
                last[i][b] = last[i+1][b]
    # print(last)

    sumi_arr = [0] * (n+1)

    for i in range(n):
        sumi_arr[i+1] = sumi_arr[i] + arr[i] ** 2

    # print(sumi_arr)
    ans = 0
    # print(check(sumi_arr, 64, 0, 2, 4))

    for i in range(n):
        mini = n
        x = 0
        bits = [i for i in range(max_bits + 1)]
        new_bits = []
        for b in bits:
            if last[i][b] == i:
                x += (2 ** b)
            else:
                mini = min(mini, last[i][b])
                new_bits.append(b)
        bits = new_bits

        l = i
        r = mini - 1

        while l < n:
            if x * x > sumi_arr[l+1] - sumi_arr[i]:
                temp = check(sumi_arr, x * x, i, l, r)
                ans += temp - l + 1
            # print(i, l, r, x, ans)
            l = r + 1
            if l >= n:
                break
            mini = n
            new_bits = []
            for b in bits:
                if last[l][b] == l:
                    x += (2 ** b)
                else:
                    mini = min(mini, last[l][b])
                    new_bits.append(b)
            bits = new_bits
            r = mini - 1
    print(ans)  

            
            


solve()