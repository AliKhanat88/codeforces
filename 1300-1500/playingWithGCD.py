from math import gcd, lcm


def solve():
    n = int(input())
    arr = [*map(int, input().split())]
    arr.append(1)
    temp_arr = [*arr]

    for i in range(1, n+1):
        temp_arr[i] = lcm(arr[i-1], arr[i])
        if gcd(temp_arr[i-1], temp_arr[i]) != arr[i-1]:
            print("NO")
            return
    print("YES")


for t in range(int(input())):
    solve()


