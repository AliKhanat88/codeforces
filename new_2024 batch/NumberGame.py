from math import sqrt

def find_odd(num):
    i = 2
    mini = 9999999999999999
    while i <= sqrt(num):
        if num % i == 0:
            if i % 2 == 1:
                mini = min(mini, i)
            if (num // i) % 2 == 1:
                mini = min(mini, num // i)
        i += 1
    if mini == 9999999999999999:
        return -1
    else:
        return mini
def solve():
    n = int(input())
    if  n == 1:
        print("FastestFinger")
        return
    if n == 2:
        print("Ashishgup")
        return
    if n % 2 == 1:
        print("Ashishgup")
        return 
    temp = find_odd(n)
    # print(temp)
    if temp != -1:
        if n // temp != 2:
            print("Ashishgup")
        else:
            print("FastestFinger")
    else:
        print("FastestFinger")

for t in range(int(input())):
    solve()