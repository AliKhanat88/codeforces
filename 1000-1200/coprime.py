from math import gcd

def highest_coprime(n, arr):
    dict = {}
    for i, value in  enumerate(arr):
        dict[value] = i + 1
    max = - 1
    for i in dict:
        for j in dict:
            if gcd(i, j) == 1 and dict[i] + dict[j] > max:
                max = dict[i] + dict[j]
    print(max)

def main():
    for i in range(int(input())):
        n= int(input())
        arr = list(map(int, input().split()))
        highest_coprime(n, arr)

main()