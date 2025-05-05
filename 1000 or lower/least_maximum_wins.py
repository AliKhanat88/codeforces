from math import floor
def print_combination(n, r, b):
    diff = floor(n / (b+1))
    temp = n - diff * (b + 1) 
    for i in range(temp):
        print("R" * (diff), end="B")
        b = b - 1
        n = n - (diff + 1)

    for i in range(b):
        print("R" * (diff-1), end="B")
        n = n - diff
    print(n * "R")
    


def main():
    t = int(input())
    for i in range(t):
        n, r, b = map(int, input().split())
        print_combination(n, r, b)
        

main()