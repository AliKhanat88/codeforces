from math import gcd, isqrt

def solve():
    n, m = map(int, input().split())

    arr = list(map(int, input().split()))
    # print("TEST")
    cur = arr[0]
    ans = 1
    rem = 998244353
    for i in range(1, n):
        if gcd(cur, arr[i]) != arr[i]:
            print(0)
            return 
        else:
            temp = cur // arr[i]
            j = 2
            done = set()
            while j <= isqrt(temp):
                if temp % j == 0:
                    temp = temp // j
                    done.add(j)
                    j = 1
                j += 1
            if temp != 1:
                if temp not in done:
                    done.add(temp)
            # print(done)


            done = list(done)
            count = m // arr[i]
            for j in range(1, 2**(len(done))):
                elem = 0
                pro = arr[i]
                for k in range(len(done)):
                    if (2 ** k) & j != 0:
                        elem += 1
                        pro = pro * done[k]
                if elem % 2 == 0:
                    count = count + m // pro
                else:
                    count = count - m // pro
                # print(pro, elem)
            cur = gcd(cur, arr[i])
            # print(count, "count")
            ans = (ans * count) % rem
    print(ans) 



for t in range(int(input())):
    solve()