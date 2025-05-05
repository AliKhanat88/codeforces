from collections import defaultdict

def solve():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    m = int(input())
    C = list(map(int, input().split()))
    D = list(map(int, input().split()))

    dicti = defaultdict(lambda:0)
    for i in range(n):
        dicti[A[i]] = B[i]

    total = 0
    for i in range(m):
        dicti[C[i]] = dicti[C[i]] - D[i]
        if dicti[C[i]] < 0:
            print(0)
            return
        elif dicti[C[i]] > 0:
            total += 1
    total += n - m
    print(2 ** total % 998244353) 

    
solve()