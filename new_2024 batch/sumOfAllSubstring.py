def solve():
    n = int(input())
    s = input()

    ans = 0
    for i in range(n):
        for j in range(i, n):
            k = i
            while k <= j:
                if s[k] == "1":
                    ans += 1
                    k += 2
                k += 1
    print(ans)


for t in range(int(input())):
    solve()