def solve():
    n, m = map(int, input().split())
    arr = [0] * n
    for i in range(n):
        arr[i] = list(input())
    
    parity = 