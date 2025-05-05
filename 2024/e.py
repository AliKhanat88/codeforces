inf = 9999999999999999999999
from pprint import pprint
def solve():
    n, m, k = map(int, input().split())
    w = int(input())
    arr = list(map(int, input().split()))

    data = [[inf for i in range(m)] for i in range(n)]
    max_i = n - k + 1
    max_j = m - k + 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            tempi = min(i, max_i)
            tempj = min(j, max_j)
            if tempi >= k:
                tempi = k
            if tempj >= k:
                tempj = k
            data[i - 1][j - 1] = min(data[i - 1][j - 1], tempi * tempj)
    
    for i in range(n, 0, -1):
        for j in range(1, m+1):
            tempi = min(max_i, n - i + 1)
            tempj = min(max_j, j)
            if tempi >= k:
                tempi = k
            if tempj >= k:
                tempj = k
            data[i - 1][j - 1] = min(data[i-1][j-1], tempi * tempj)
    
    for i in range(n, 0, -1):
        for j in range(m, 0, -1):
            tempi = min(max_i, n - i + 1)
            tempj = min(max_j, m - j + 1)
            if tempi >= k:
                tempi = k
            if tempj >= k:
                tempj = k
            data[i - 1][j - 1] = min(data[i-1][j-1], tempi * tempj)
    temp_arr = []

    for i in range(1, n+1, 1):
        for j in range(m, 0, -1):
            tempi = min(max_i, i)
            tempj = min(max_j, m - j + 1)
            if tempi >= k:
                tempi = k
            if tempj >= k:
                tempj = k
            data[i - 1][j - 1] = min(data[i-1][j-1], tempi * tempj)
            temp_arr.append(data[i-1][j-1])
    
    
    temp_arr.sort(reverse=True)
    arr.sort(reverse=True)
    
    # if n == 9 and m == 5:
    #     pprint(data)
    #     print(temp_arr)
    ans = 0
    for i in range(len(arr)):
        ans += (temp_arr[i] * arr[i])
    print(ans)




    
        

for t in range(int(input())):
    solve()