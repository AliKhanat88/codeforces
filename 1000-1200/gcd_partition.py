from math import gcd

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = input().split()
        arr[0] = int(arr[0])
        for j in range(1, n):
            arr[j] = int(arr[j]) + arr[j-1]
        ans = 1
        for j in range(n-2, -1, -1):
            temp = gcd(arr[-1], arr[j])
            ans = max(ans, temp)
        print(ans)
main()