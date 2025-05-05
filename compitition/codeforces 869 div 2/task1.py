import sys
input = sys.stdin.readline

def print_max(n, k, data):
    max_min = [0]*k
    for i in range(k):
        plus = 0
        minus = 0
        for j in range(n):
            if data[i][j] == "+":
                plus += 1
            else:
                minus += 1
        if plus >= 

for t in range(int(input())):
    n, k = map(int, input().split())
    data = [0] * n
    for i in range(n):
        data[i] = input()
    print_max(n, k, data)   
