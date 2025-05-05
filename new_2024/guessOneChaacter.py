import sys
input = sys.stdin.readline

INF = float('inf')
MOD = 10**9 + 7


def ask(a,b):
    print(f'{a} {b}')
    sys.stdout.flush()
    o = int(input().strip())
    if o == -1: quit()
    return o

def ans(v):
    print(0,1,v)
    sys.stdout.flush()
    input()


# 001010110

def solve():
    n, = map( int , input().strip().split() )
    ones = ask(1,1)

    gr = ones - ask(1,11)

    prv = ask(1,'01')

    if gr == prv:
        ans(0)
    else:
        ans(1)
    



for i in range(int(input().strip())):
    solve()