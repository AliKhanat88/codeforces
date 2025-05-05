import sys
sys.setrecursionlimit(100000)

def solve():
    n, h = map(int, input().split())
    arr = [*map(int, input().split())]
    arr.sort()
    ans = [0]
    def recur(i, h, g, b):
        if i >= n:
            ans[0] = max(ans[0], i)
            return
        else:
            while i < n:
                if h > arr[i]:
                    h += (arr[i] // 2)
                    i += 1
                else:
                    break
            ans[0] = max(ans[0], i)
            if g != 0 or b != 0:
                if g > 0:
                    recur(i, h*2, g-1, b)
                if b > 0:
                    recur(i, h*3, g, b-1)
    
    recur(0, h, 2, 1)
    print(ans[0])
            
for t in range(int(input())):
    solve()