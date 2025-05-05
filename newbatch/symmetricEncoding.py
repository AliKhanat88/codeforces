from collections import defaultdict

def solve():
    n = int(input())
    s = input()
    s_s = sorted(list(set(s)))

    dict = defaultdict(lambda: 0)

    for i in range(len(s_s)):
        dict[s_s[i]] = s_s[len(s_s) - i - 1]

    # print(dict)

    for i in range(n):
        print(dict[s[i]],end="")
    print()



for t in range(int(input())):
    solve()