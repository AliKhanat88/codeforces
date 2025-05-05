from math import ceil
def sol():
    n = int(input())
    sumi = 0
    while n > 0:
        sumi += n
        n = n // 2
    print(sumi)
for t in range(int(input())):
    sol()