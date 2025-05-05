import sys
input = sys.stdin.readline

def solve():
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))

    prefix = [0] * (n + 1)

    for num in arr:
        prefix[num] += 1
    # print(prefix)
    for i in range(1, n+1):
        prefix[i] += prefix[i-1]
    
    # print(prefix)

    def get_less(num, x):
        org_num = num
        out =  prefix[num]
        # print("get_less", num, x)
        num += x
        while num <= n:
            out += (prefix[num] - prefix[num // x * x - 1])
            num += x
        if num == n:
            return out
        if num // x * x <= n:
            out += (prefix[min(num // x * x + org_num, n)] - prefix[num // x * x - 1])
        # print(out)
        return out
    
    def bin(x):
        l = 0
        r = x - 1
        comp = (n + 2) // 2
        while l + 1 < r:
            mid = (l + r) // 2
            temp = get_less(mid, x)
            if temp >= comp:
                r = mid
            else:
                l = mid + 1
        temp = get_less(l, x)
        if temp >= comp:
            return l
        temp = get_less(r, x)
        if temp >= comp:
            return r
    

        


    ans = [-1] * (n + 1)
    for i in range(q):
        ques = int(input())
        if ans[ques] == -1:
            ans[ques] = bin(ques)
        print(ans[ques], end=" ")
    print()



for t in range(int(input())):
    solve()