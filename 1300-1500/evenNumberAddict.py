from math import ceil
def solve():
    n = int(input())
    arr = [*map(int, input().split())]
    even = 0
    odd = 0
    for i in range(n):
        if arr[i] % 2 == 0:
            even += 1
        else:
            odd += 1
    
    if ceil(odd / 2) % 2 == 0:
        print("Alice")
    elif ceil(odd / 2) % 2 == 1 and (odd - ceil(odd / 2)) % 2 == 1:
        print("Bob")
    elif even % 2 == 1 and ceil(odd / 2) % 2 == 1:
        print("Alice")
    else:
        print("Bob")

for i in range(int(input())):
    solve()