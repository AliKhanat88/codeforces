from collections import defaultdict
import sys
input = sys.stdin.readline

def solve():
    dict = defaultdict(lambda:0)
    n = int(input())
    ans = 0
    for i in range(n):
        a, b = map(int, input().split())
        dict[(1,a)] += 1
        ans += dict[(1,a)] * (dict[(1,a)] - 1) - (dict[(1,a)] - 1) * (dict[(1,a)] - 2)
        dict[(2, b)] += 1
        ans += dict[(2, b)] * (dict[(2, b)] - 1) - (dict[(2, b)] - 1) * (dict[(2, b)] - 2)
        dict[(3, a-b)] += 1
        ans += dict[(3, a-b)] * (dict[(3, a-b)] - 1) - (dict[(3, a-b)] - 1) * (dict[(3, a-b)] - 2)
        dict[(4, a+b)] += 1
        ans += dict[(4, a+b)] * (dict[(4, a+b)] - 1) - (dict[(4, a+b)] - 1) * (dict[(4, a+b)] - 2)

    # print(dict1)
    # print(dict2)
    # print(dict3)
    # print(dict4)
    print(ans)
for t in range(int(input())):
    solve()