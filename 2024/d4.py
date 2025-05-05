import sys
input = sys.stdin.readline
from bisect import insort_left

def solve():
    n, m = map(int, input().split())
    maxi = -1
    for i in range(n):
        arr = list(map(int, input().split()))
        arr.pop(0)
        arr.sort()
        # Initialize mex to 0
        mex = 0

        # Iterate through the sorted array
        for num in arr:
            if num == mex:
                mex += 1
            elif num > mex:
                break
        
        arr.append(mex)
        arr.sort()
        mex = 0
        for num in arr:
            if num == mex:
                mex += 1
            elif num > mex:
                break

        

                
        maxi = max(maxi, mex)
    # print(maxi)
    if maxi >= m:
        print(maxi * (m + 1))
    else:
        print(maxi * (maxi) + ((m + maxi) * (m - (maxi) + 1)) // 2)




for t in range(int(input())):
    solve()