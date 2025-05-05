import sys
input = sys.stdin.readline

def print_poss(n, one, two):
    i = 0
    while i < n:
        if one[i] == "W":
            cur = False
            break
        elif two[i] == "W":
            cur = True
            break
        i += 1
    i = i + 1
    for i in range(i, n):
        if one[i] == "W":
            if cur == True:
                print("NO")
                return
        elif two[i] == "W":
            if cur == False:
                print("NO")
                return
        else:
            cur = not cur
    print("YES")
        
for t in range(int(input())):
    n = int(input())
    one = input().rstrip()
    two = input().rstrip()
    print_poss(n, one, two)
