def solve():
    n, c, q = map(int, input().split())
    s = input()
    dict = {}
    k = len(s) + 1
    for i in range(c):
        a, b = map(int, input().split())
        dict[(k, k+b-a)] = (a, b)
        k = k + b - a + 1

    items = dict.items()
    # print(items)
    for i in range(q):
        a = int(input())
        while a > n:
            for num in items:
                if a <= num[0][1] and a >= num[0][0]:
                    a = num[1][0] + a - num[0][0]
                    # print(a)
                    break
        print(s[a-1])

for t in range(int(input())):
    solve()