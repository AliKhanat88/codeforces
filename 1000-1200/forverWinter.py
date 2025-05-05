from collections import defaultdict

def print_xy(n, m):
    dict = defaultdict(lambda:0)
    for i in range(m):
        a, b = map(int, input().split())
        dict[a] += 1
        dict[b] += 1 
    leaves = 0
    for num in dict.values():
        if num == 1:
            leaves += 1
    print(n-leaves-1, leaves // (n-leaves-1))
for t in range(int(input())):
    n, m = map(int, input().split())
    print_xy(n, m)