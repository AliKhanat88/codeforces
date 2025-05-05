from math import floor, sqrt, isqrt
for t in range(int(input())):
    l, r = map(int, input().split())
    num1 = isqrt(l)
    count1 = num1 * 3 - 3
    num = num1 ** 2
    for i in range(3):
        if num < l:
            count1 += 1
        else:
            break
        num += num1
    num2 = isqrt(r)
    count2 = num2 * 3 - 3
    num = num2 ** 2
    for i in range(3):
        if num <= r:
            count2 += 1
        else:
            break
        num += num2
    print(count2 - count1)