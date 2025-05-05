from collections import defaultdict
def solve(n, a, b):
    dict = defaultdict(lambda:0)
    for char in a:
        dict[char] += 1
    for char in b:
        dict[char] -= 1
    if n <= 5:
        for i, char in enumerate(a):
            if i < 3 and n-i-1 < 3 and b[i] != char:
                print("NO")
                return
    set_val = list(set(dict.values()))
    for num in set_val:
        if num != 0:
            print("NO")
            return
    print("YES")

for t in range(int(input())):
    n, k = map(int, input().split())
    a = input()
    b = input()
    solve(n, a, b)
                
