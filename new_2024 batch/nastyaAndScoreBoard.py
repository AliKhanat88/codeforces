from collections import defaultdict

import sys

input = sys.stdin.readline

dict_dp = defaultdict(lambda:-1)

dict = {
    "1110111": 0, 
    "0010010": 1,
    "1011101": 2,
    "1011011": 3,
    "0111010": 4,
    "1101011": 5,
    "1101111": 6,
    "1010010": 7,
    "1111111": 8,
    "1111011": 9
}

def findNums(s):
    if dict_dp[s] != -1:
        return dict_dp[s]
    l = []
    for key, val in dict.items():
        k = 0
        isTrue = True
        # print(key,val)
        for i in range(7):
            if s[i] == "1" and key[i] == "0":
                isTrue = False
                break
            elif s[i] != key[i]:
                k += 1
        if isTrue:
            l.append((val, k))
    dict_dp[s] = l
    return dict_dp[s]

# print(findNums("1001001"))
n, k = map(int, input().split())
arr = [0] * n
for i in range(n):
    arr[i] = input()

dp = [[-1 for i in range(k+1)] for i in range(n)]

temp = findNums(arr[0])
# print(dp)
for num in temp:
    if num[1] <= k:
        dp[0][num[1]] = num[0]

for i in range(1,n):
    temp = findNums(arr[i])
    if len(temp) != 0:
        for j in range(k, -1, -1):
            for num in temp:
                if dp[i-1][j] != -1 and num[1] + j <= k:
                    if dp[i][num[1] + j] < dp[i-1][j]* 10 + num[0]:
                        dp[i][num[1] + j] = dp[i-1][j]* 10 + num[0]

# print(dp)
print(dp[n-1][k])
        

