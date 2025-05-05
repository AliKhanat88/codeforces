

def fun(x):
    ans = x // 4 + 1
    if x % 4 > 1:
        ans += 1
    return x - ans -1
# print(fun(7))
n = int(input())
if n == 1:
    print(3)
    exit()
low = n 
high = 5 * n
while high >= low:
    mid = (high - low) // 2 + low
    if fun(mid) == n:
        if mid % 2 == 0 and mid % 4 != 0:
            print(mid - 1)
        else:
            print(mid)
        exit()
    elif fun(mid) > n:
        high = mid - 1
    else:
        low = mid + 1

