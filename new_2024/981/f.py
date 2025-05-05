MOD = 10 ** 9+7

def solve():
    n, k = map(int, input().split())
    if k == 1:
        print(n % MOD)
        return
    per_0 = 1
    per_1 = 1
    ans_1 = None
    for i in range(1, k * k + 1):
        temp1 = (per_1 + per_0) % k
        per_1 = temp1 
        per_0 = per_1
        if per_1 % k == 0:
            ans_1 = i + 2
            break
    print(ans_1)
    if ans_1 == None:
        raise Exception()
    print((ans_1 * n) % MOD)



for t in range(int(input())):
    solve()