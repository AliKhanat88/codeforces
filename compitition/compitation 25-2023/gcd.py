from math import gcd
   
def check_gcd(n, arr):
    for i in range(n):
        for j in range(i+1, n):
            if gcd(arr[i], arr[j]) <= 2:
                print("YES")
                return
    print("NO")


def main():
    for i in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        check_gcd(n, arr)

main()