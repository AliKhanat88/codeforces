from math import gcd

def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    if n == 1:
        if k > arr[0]:
            print(k)
        else:
            print(k-1)
        return
    gc = gcd(*arr)
    new_arr = [0] * n
    for j in range(n):
        new_arr[j] = j * gc
    # print(new_arr)
    # ans = 0
    for i in range(1, n):
        if k > new_arr[i] - new_arr[i-1] - 1:
            k -= (new_arr[i] - new_arr[i-1] - 1)
        else:
            print(new_arr[i-1] + k)
            return 
    print(new_arr[-1] + k)


for t in range(int(input())):
    solve()