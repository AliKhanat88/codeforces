from math import isqrt

def checkHowMany(arr, x):
    count = 0
    for i in range(len(arr)):
        temp = isqrt((arr[i] + x))
        if (arr[i] + x) == temp * temp:
            count += 1
    return count

def solve():
    k = int(input())
    arr = list(map(int, input().split()))
    if k == 1:
        print(1)
        return
    # print("TEST")
    arr.sort()
    maxi = 1
    for i in range(k):
        for j in range(i+1, k):
            a = arr[j]
            b = arr[i]
            n = 1
            while (3 + n + 1) * n <= a - b:
                if ((a - b) - (2 * n) + (n ** 2)) % (2 * n) == 0:
                    n1 = ((a - b) - (2 * n) + (n ** 2)) // (2 * n)
                    x = 2 * n1 + n1 ** 2 - a + 1
                    if x >= 0 and x % 1 == 0 and x <= 10 ** 18:
                        # print("x", x, "n", n, "n1", n1, "a", a, "b", b)
                        maxi = max(maxi, checkHowMany(arr, int(x)))
                n += 1
    
    print(max(maxi, checkHowMany(arr, 0)))

for t in range(int(input())):
    solve()