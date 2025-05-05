import sys
input = sys.stdin.readline

def check9(x):
    while x > 0:
        if x % 10 == 7:
            return True
        x = x // 10
    return False
def solve():
    n, = map(int, input().split())
    mini = 20
    if check9(n) == True:
        mini = 0
    for i in range(1, 11):
        x = n
        for j in range(10):
            x += 10 ** i - 1
            if check9(x):
                mini = min(mini, j+1)
    print(mini)




    





for t in range(int(input())):
    solve()