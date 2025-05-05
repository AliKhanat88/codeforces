def solve():
    n = int(input())
    rem = n % 11
    if n - rem * 111 < 0:
        print("NO")
    else:
        print("YES")


for t in range(int(input())):
    solve()