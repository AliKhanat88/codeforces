
    
def solve():
    ans = []
    x = int(input())

    while x > 0:
        if x % 2 == 0:
            ans.append(0)
        elif x % 4 == 1:
            ans.append(1)
            x -= 1
        elif x % 4 == 3:
            ans.append(-1)
            x += 1
        x = x // 2
    print(len(ans))
    print(*ans)

for i in range(int(input())):
    solve()