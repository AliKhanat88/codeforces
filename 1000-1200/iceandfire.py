import sys
input = sys.stdin.readline

def print_comb(n, s):
    per = 1
    print(per, end= " ")
    for i in range(1, n-1):
        if s[i] == s[i-1]:
            print(per, end= " ")
        else:
            print(i+1, end=" ")
            per = i + 1
    print()
for t in range(int(input())):
    n = int(input())
    s = input().rstrip()
    print_comb(n, s)