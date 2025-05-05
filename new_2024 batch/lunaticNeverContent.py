from math import gcd

def print_max(n, arr):
    per = None
    i = 0
    k = n-1
    while i < k:
        if arr[i] != arr[k]:
            temp = max(arr[i], arr[k]) - min(arr[i], arr[k])
            if per == None:
                per = temp
            else:
                per = gcd(temp, per)
        i += 1
        k -= 1 
    if per == None:
        print(0)
    else:
        print(per)

for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print_max(n, arr)