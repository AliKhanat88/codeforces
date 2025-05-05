import sys
input = sys.stdin.readline


def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    for i in range(n):
        can = True
        for j in range(n):
            if i != j:
                if abs(arr[i] - arr[j]) % k == 0:
                    can = False
                    break
        if can:
            print("YES")
            print(i + 1)
            return
    print("NO")


for t in range(int(input())):
    solve()