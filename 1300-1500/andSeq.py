from math import comb, factorial
# def factorial(num1, num2):
#     product = 1
#     for i in range(num1, 1, -1):
#         product = (product * i) % 1000000007

#     for i in range(num2, 1, -1):
#         product = (product * i) % 1000000007
#     print(product % 1000000007)
def solve():
    n = int(input())
    arr = list(map(int,input().split()))

    andi = arr[0]
    for i in range(1, n):
        andi = andi & arr[i]
    num1 = arr.count(andi)
    num2 = n - 2
    if num1  < 2:
        print(0)
        return
    print(2 * (comb(num1, 2) * factorial(num2)) % 1000000007)




for t in range(int(input())):
    solve()