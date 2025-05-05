def check_max_sub_sum(arr):
    new_arr = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        new_arr[i+1] = max(0, new_arr[i] + arr[i])
    return new_arr

def solve(n, k, x, arr):
    if x >= 0:
        maxi = 0
        new_arr = check_max_sub_sum([num - x for num in arr])
        # print([num - x for num in arr])
        # print(new_arr)
        for i in range(n - k + 1):
            other_maxi = new_arr[i]
            for j in range(i, i + k):
                other_maxi += arr[j] + x
                if other_maxi < 0:
                    other_maxi = 0
                maxi = max(maxi, other_maxi)
        
        print(maxi)
        return maxi
    else:
        maxi = 0
        for i in range(k+1):
            temp_arr = [num - x for num in arr]
            for j in range(i):
                temp_arr[j] += (x * 2)
            for j in range(k - i):
                temp_arr[n-j-1] += (x*2)
            maxi = max(maxi, max(check_max_sub_sum(temp_arr)))
            # print(maxi)
        print(maxi)
        return maxi
    
# from itertools import combinations

def brute(n, k, x, a):
    L=-10**15
    dp=[[L]*(n+1) for _ in range(k+2)]
    dp[0][0]=0
    ans=0
    for i in range(1,n+1):
        for j in range(0,k+1):
            if j>i or j+n-i<k:continue
            dp[j][i]=max(dp[j][i-1]+a[i-1]-x,0,dp[j-1][i-1]+a[i-1]+x)
            ans=max(ans,dp[j][i])
    return ans

from random import randint
def checker():
    n = 50
    for i in range(100000):
        arr = [randint(-100, 100) for i in range(n)]
        k = randint(1, n)
        x = randint(-100, 100)
        # print(brute(n, k, x, arr[:]), solve(n, k, x, arr[:]))
        if brute(n, k, x, arr[:]) != solve(n, k, x, arr[:]):
            print("Found")
            print(1)
            print(n, k, x)
            print(*arr)
            return
        

# for t in range(int(input())):
#     n, k, x = map(int, input().split())
#     arr = list(map(int, input().split()))
#     solve(n, k, x, arr)

checker()