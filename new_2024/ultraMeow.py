from math import comb

MOD = 10**9+7

def solve():
    n = int(input())
    ans = 0
    factorial = [1] * (2 * n + 1)
    fact_inverse = [1] *(2 * n + 1)
    for i in range(1, 2 * n + 1):
        factorial[i] = (factorial[i-1] * i) % MOD
        fact_inverse[i] = pow(factorial[i], -1, MOD)
    
    for i in range(1, n+n+2):
        for j in range(min(i-1, n), -1, -1):
            if i - j - 1 > j:
                break
            gre = max(0, n - i)
            less = min(n, i - 1)
            less_req = i - j - 1
            grea_req = j - (i - j - 1)
            if less_req > less or less_req < 0 or grea_req > gre or grea_req < 0:
                continue
            first = factorial[min(n, i - 1)] *fact_inverse[i - j - 1] * fact_inverse[min(n, i - 1) - (i - j - 1)]
            second = factorial[max(0, n - i)] * fact_inverse[max(0, j - (i - j - 1))]  * fact_inverse[max(0, n - i) - max(0, j - (i - j - 1))]
            ans = (ans +  first * second * i) % MOD
            # print(i, j,l, g, comb(min(n, i - 1), i - j - 1), comb(max(0, n - i), max(0, j - (i - j - 1))))

    
    print(ans % MOD)


for t in range(int(input())):
    solve()