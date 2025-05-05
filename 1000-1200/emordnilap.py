from math import factorial

for t in range(int(input())):
    n = int(input())
    temp = (n * (n -1) ) * factorial(n)
    print(temp % 1000000007)