from math import gcd

def solve():
    n, a, b = map(int, input().split())
    arr = list(map(int, input().split()))
    k = gcd(a, b)
    arr.sort()
    maxi = arr[-1]
    mini = arr[-1]
    for i in range(n-1):
        temp1 = arr[-1] - (arr[-1] - arr[i]) % k 
        temp2 = temp1 + k
        if temp1 >= mini and temp1 <= maxi:
            arr[i] = temp1
        elif temp2 >= mini and temp2 <= maxi:
            arr[i] = temp2
        
        maxi = max(maxi, arr[i])
    print(arr)
    print(max(arr) - min(arr))

for t in range(int(input())):
    solve()