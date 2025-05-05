def solve():
    n, a, b = map(int, input().split())
    s = input()
    x, y = 0, 0
    for i in range(20):
        for i in range(n):
            if s[i] == "N":
                y += 1
            elif s[i] == "E":
                x += 1
            elif s[i] == "S":
                y -= 1
            elif s[i] == "W":
                x -= 1
            if x == a and y == b:
                print("YES")
                return
    print("NO")
for t in range(int(input())):
    solve()