from math import sqrt

def roots(b, c):
    # print(b, c)
    temp = sqrt(b ** 2 - 4 * c)
    return ((- b + temp) / 2 , (-b - temp) / 2)

def kth_position(n, d, a0):
    return int(n * a0 + d * n * (n-1) / 2)

def solve():
    a, b, c, k = map(int, input().split())
    if a > c or b > c:
        print(-1)
        return
    elif len(str(int("9"*a) + int("9"*b))) < c:
        print(-1)
        return
    elif a == c or b == c:
        maxi = int("9" * c)
        a0 = maxi - 10 ** (b-1) 
        start_a = 10 ** (a-1)
        start_b = 10 ** (b-1)
        # print(start_a, start_b , a0)
        real = int(roots(2 * a0 - 1, -2 * k)[0])
        # print(real)
        print(real + start_a, start_b + k - kth_position(real, -1, a0) -1)
    else:
        start = 10 ** (c-1)
        if a <= b:
            maxi = 10 ** (a)
            a0 = maxi - 10 ** (a-1)
            start_a = 10 ** (a-1)
            start_b = start - 10 ** (a-1)
            # print(start_a, start_b, a0)
            real = int(roots(2 * a0 - 1, -2 * k)[0])
            # print(real)
            print(real + start_a , start_b + k - kth_position(real, -1, a0) -1)
        else:
            max_b = int("9" * b)
            start_a = 10 ** (c-1) - max_b
            a0 = 1
            # print(start_a, max_b, a0)
            real = int(roots(2 * a0 - 1, -2 * k)[1])
            # print(real)
            print(real + start_a , k - kth_position(real, -1, a0))


for t in range(int(input())):
    solve()