
from collections import defaultdict

prime = [1] * 1000000
dicti = {}
for i in range(3, 500001, 2):
    j = i + i
    while j <= 1000000:
        if prime[j-1] != -1:
            dicti[j] = i
            prime[j-1] = -1
        j += i
    
for t in range(int(input())):
    n, m = map(int, input().split())
    # print(dicti[n])
    # print(prime[n-1])
    if m == 1:
        print("YES")
    elif n == 1:
        print("YES")
    elif m >= n:
        print("NO")
    elif n % 2 == 1 and prime[n-1] == 1:
        print("YES")
    elif n % 2 == 1 and prime[n-1] == -1 and dicti[n] > m:
        print("YES")
    else:
        print("NO")