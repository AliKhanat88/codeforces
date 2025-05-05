import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    c = list(map(int, input().strip().split()))
    arr = [0] * (n+1)
    for i in range(n):
        arr[a[i]] = i
    ans = 1
    for i in range(n):
        if a[i] != -1 and a[i] != b[i]:
            temp = arr[b[i]]
            if c[i] == 0:
                can = True
            else:
                can = False
            while b[temp] != a[i]:
                a[temp] = -1
                if c[temp] != 0:
                    can = False
                temp = arr[b[temp]]
            a[temp] = -1
            if can and c[temp] == 0:
                ans *= 2
        # print(a)
    print(ans % 1000000007)
                



for t in range(int(input())):
    solve()