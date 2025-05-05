from math import log2
def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        power = log2(n)
        if power % 1 == 0:
            power = int(power - 1)
        else:
            power = int(power)
        for i in range(n-1, 2**power-1, -1):
            print(i, end=" ")
        for i in range(2**power):
            print(i, end=" ")
        print()

main()
