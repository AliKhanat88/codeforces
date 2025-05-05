from math import factorial

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        sum = n * (n-1)
        sum = sum * factorial(n)
        print(sum % 1000000007)

main()