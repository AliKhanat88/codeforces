from collections import Counter

def solve():
    n, x, y = map(int, input().split())
    arr = list(map(int, input().split()))
    c = Counter()
    ans = 0
    for num in reversed(arr):
        ans += c[((x - num%x) %x, num%y)]
        c[(num%x, num%y)] += 1
        # print(c, ans)
    print(ans)
        
for t in range(int(input())):
    solve()