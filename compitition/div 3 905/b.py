from collections import defaultdict

def solve():
    n, k = map(int, input().split())
    s = input()

    dict = defaultdict(lambda:0)

    for char in s:
        dict[char] += 1

    evens = 0
    for key, val in dict.items():
        if val % 2 == 1:
            evens += 1
    if evens > k + 1:
        print("NO")
        return
    print("YES")
    

for t in range(int(input())):
    solve()