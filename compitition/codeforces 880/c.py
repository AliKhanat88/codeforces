from math import sqrt

def sol(x):
    return (sqrt(1 + x*8) - 1) / 2

print(sol(int(input())))