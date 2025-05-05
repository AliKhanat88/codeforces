from math import gcd

def check(arr):
    per = -1
    for i in range(1, len(arr)):
        temp = gcd(arr[i], arr[i-1])
        if temp < per:
            return False
        per = temp
    return True

def solve():
    n = int(input())

    arr = list(map(int, input().split()))
    per = -1
    for i in range(1, n):
        temp = gcd(arr[i], arr[i-1])
        if temp < per:
            for j in range(i, max(-1, i-5), -1):
                arr_t = arr[:]
                arr_t.pop(j)
                if check(arr_t) == True:
                    print("YES")
                    return
            
            for j in range(i, min(n, i+5)):
                arr_t = arr[:]
                arr_t.pop(j)
                if check(arr_t) == True:
                    print("YES")
                    return
            print("NO")
            return
        per = temp
    print("YES")

            
for t in range(int(input())):
    solve()
