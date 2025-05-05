import sys
input = sys.stdin.readline
def get_art(mid, n):
    return ((n + mid) * (n - mid + 1)) // 2

def get_less(x, n):
    l = 1
    r = n
    while l + 1 < r:
        mid = (l + r) // 2
        if get_art(mid, n) < x:
            r = mid
        else:
            l = mid + 1
    
    if get_art(mid, n) < x:
        return n - r + 1
    else:
        return n - l + 1

def solve():
    n = int(input())
    arr = list(map(int, input().strip().split()))
    mega_prefix = [0] * (n + 1)
    mini_prefix = [0] * (n + 1)
    sumi = 0
    per = 0
    for i in range(n):
        per += arr[i]
        mini_prefix[i+1] = mini_prefix[i] + per
        sumi += per
    
    for i in range(1, n+1):
        mega_prefix[i] = sumi
        sumi = sumi - (arr[i-1] * (n + 1 - i))
    
    print(mini_prefix)
    print(mega_prefix)
    print(get_less(5, n))
    print(get_less(8, n))

    for i in range(int(input())):
        l, r = map(int, input().split())
        l_i = get_less(l, n)
        r_i = get_less(r, n)
        ans = mega_prefix[r_i] - mega_prefix[l_i]
        


    

for t in range(int(input())):
    solve()