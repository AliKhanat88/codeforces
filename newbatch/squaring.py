from decimal import Decimal, getcontext
getcontext().prec = 15
num = 10 ** 20
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    # print("TEST")
    isOne = False
    for i in range(n):
        if arr[i] == 1:
            if isOne:
                print(-1)
                return
        else:
            isOne = True
    
    power = [0] * n
    # print(arr)
    ans = 0
    # print(arr)
    for i in range(1, n):
        l = power[i]
        r = power[i-1] + 30
        temp = pow(arr[i-1], pow(2, power[i-1]))
        while l + 1 < r:
            m = (l + r) // 2
            if pow(arr[i], pow(2, m)) >= temp:
                r = m
            else:
                l = m + 1
        if pow(arr[i], pow(2, l)) >= temp:
            ans += l - power[i]
            power[i] = l
        else:
            ans += r - power[i]
            power[i] = r

            
    print(ans)

for t in range(int(input())):
    solve()