from math import gcd

def check_gcd(n, arr):
    per = arr[0]
    for i in range(1, n):
        if arr[i-1] % arr[i] == 0:
            temp2 = arr[i-1]
        elif arr[i] % arr[i-1] == 0:
            temp2 = arr[i]
        else:
            temp2 = arr[i-1] * arr[i]
        temp1 = per
        temp3 = gcd(temp1, temp2)
        if temp3 != arr[i-1]:
            print("NO")
            return
        per = temp2
    print("YES")
def main():
    for i in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        check_gcd(n, arr)

main()
