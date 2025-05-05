from math import log2, floor
for t in range(int(input())):
    a, b = map(int, input().split())
    maxi = 0
    for i in range(0, floor(log2(b))+1):
        temp = 2 ** i
        # print(temp, "bit")
        lower = a // temp
        if (lower) % 2 == 1:
            ans = temp * lower - a 
        else:
            ans = 0
            lower = lower + 1
        higher = b // temp
        if (higher) % 2 == 1:
            ans = ans + (b - temp * higher + 1) 
        else:
            higher = higher + 1
        ans += (higher* temp - lower* temp) // 2
        maxi =max(ans, maxi)
    print(b - a - maxi+ 1)
        
        