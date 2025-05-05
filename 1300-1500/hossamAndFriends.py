from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    dict = defaultdict(lambda:-1)
    for i in range(m):
        a, b = map(int, input().split())
        if a > b:
            mini = b
            maxi = a
        else:
            mini = a
            maxi = b
        dict[maxi] = max(mini, dict[maxi])

    ans = 0
    per = 1

    # middle count
    for i in range(1, n+1):
        if dict[i] != -1:
            per = max(per, dict[i] + 1)
        ans += i - per + 1
        # print(ans, i)

    # print(dict)
    print(ans)
        



for t in range(int(input())):
    solve()