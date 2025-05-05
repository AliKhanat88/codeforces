from copy import deepcopy

n = int(input())

arr = list(map(int, input().split()))

dp = {}

def recur(n, arr):
    if n <= 1:
        return 0
    else:
        
        
        mini = 9999999999999999999999999
        for i in range(1, n):
            temp = deepcopy(arr)
            temp[i] = temp[i] + temp[i-1]
            temp1 = temp[i]
            temp.pop(i-1)
            mini = min(mini, recur(n-1, temp) + temp1)
        dp[temp2] = mini
        return mini
    
print(recur(n, arr))
print(dp)
