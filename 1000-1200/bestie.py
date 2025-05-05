from math import gcd
def find_gcd(n, arr):
    gcd_num = arr[0]
    for i in range(1, n):
        gcd_num = gcd(gcd_num, arr[i])
    return gcd_num

def check_gcd(n, arr):
    gcd_num = find_gcd(n, arr)
    if gcd_num == 1:
        print(0)
        return 
    temp = arr[-1]
    arr[-1] = gcd(arr[-1], n)
    gcd_num = find_gcd(n, arr)
    if gcd_num == 1:
        print(1)
        return
    arr[-1] = temp
    temp = arr[-2]
    arr[-2] = gcd(arr[-2], n-1)
    gcd_num = find_gcd(n, arr)
    if gcd_num == 1:
        print(2)
        return
    print(3)

def main():
    for i in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        check_gcd(n, arr)

main()