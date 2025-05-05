import sys
input = sys.stdin.readline

def print_pair(n, arr):
    first = arr[0] % 2 == 0
    last = None 
    count = 0
    i = n-1
    print(n-1)
    while i >= 0:
        if (arr[i] % 2 == 0) == first:
            if last != None:
                print(i+1, last+1)
                last = i
                count += 1
            else:
                last = i
        i-=1
    for i in range(1, n):
        if (arr[i] % 2 == 0) != first:
            print(1, i+1)
    
for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print_pair(n, arr)