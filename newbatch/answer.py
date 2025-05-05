from collections import Counter

def solve():
    n = int(input())
    s = Counter(list(input()))
    ans = 0
    for i in range(ord("A"), ord("E")):
        temp = s[chr(i)]
        if temp >= n:
            ans += n
        else:
            ans += temp
    print(ans)

for t in range(int(input())):
    solve()