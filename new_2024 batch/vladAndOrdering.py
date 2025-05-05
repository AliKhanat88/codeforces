from math import ceil
def solve():
    n, k = map(int, input().split())
    if ceil(n / 2) >= k:
        print(2 * k-1)
    else:
        k = k - ceil(n / 2)
        i = 1
        while 2 ** i <= n:
            temp = n // (2 ** i) - n // (2 ** (i+1))
            if temp >= k:
                print((2 ** (i+1)) * k - 2 ** i)
                return
            k -= temp
            i += 1
    

for t in range(int(input())):
    solve()