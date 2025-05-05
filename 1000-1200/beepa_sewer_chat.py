import sys
input = sys.stdin.readline

def print_mini(n, first, second):
    i = n - 1
    j = n - 1
    while i >= 0 and j >= 0:
        if second[i] == first[j]:
            i -= 1
            j -= 1
        else:
            j -= 1
    print(i+1)
        
        

for t in range(int(input())):
    n = int(input())
    first = list(map(int, input().split()))
    second = list(map(int, input().split()))
    print_mini(n, first, second)