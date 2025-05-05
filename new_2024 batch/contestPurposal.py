def check(a, b):
    for i in range(len(a)):
        if a[i] > b[i]:
            return False
    return True

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if check(a, b):
            print(ans)
            return
        else:
            a = [0] + a
            a.pop()
            ans += 1
    print(ans)

for t in range(int(input())):
    solve()