import math 
def main():
    n = int(input())
    for i in range(n):
        n, a, b = map(int, input().split())
        if b < a:
            print(1)
        else:
            print(math.ceil(n / a))

main()