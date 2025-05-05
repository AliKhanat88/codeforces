import sys
input = sys.stdin.readline

dict_index = {
    "n": 0,
    "a": 1,
    "r": 2,
    "e": 3,
    "k": 4
}

inf = -99999999999999999999999999

def solve():
    n, m = map(int, input().strip().split())
    arr = []
    for i in range(n):
        arr.append(input().strip())

    # print(arr)

    counts = [0] * n
    count_5 = []
    last_ind = []
    for i in range(n):
        temp = [0, 0, 0 ,0 ,0]
        temp_ind = [0, 1, 2, 3, 4]
        count = 0
        for j in range(m):
            if arr[i][j] in ["n","a","r","e","k"]:
                count += 1
                for k in range(5):
                    
                    if dict_index[arr[i][j]] == temp_ind[k]:
                        temp_ind[k] += 1
                        if temp_ind[k] == 5:
                            temp_ind[k] = 0
                            temp[k] += 1
        counts[i] = count
        count_5.append(temp)
        last_ind.append(temp_ind)
            # print(temp)
            # print(temp_ind)
    # print(counts)
    # print(count_5)
    # print(last_ind)

    dp = [inf] * 5
    
    for i in range(n):
        per_dp = dp[:]
        for char in range(5):
            for last in range(5):
                if last_ind[i][last] != last or count_5[i][last] != 0:
                    if (last < last_ind[i][char] or last == 4):
                        dp[last] = max(dp[last], per_dp[char - 1] + count_5[i][char] * 10 - counts[i])
                    else:
                        dp[last] = max(dp[last], per_dp[char - 1] + (count_5[i][char] - 1) * 10 - counts[i])
        for last in range(5):
            if last_ind[i][last] != last or count_5[i][last] != 0:
                if last < last_ind[i][0] or last == 4:
                    dp[last] = max(dp[last], count_5[i][0] * 10 - counts[i])
                else:
                    dp[last] = max(dp[last], (count_5[i][0] - 1) * 10 - counts[i])
        # print(dp)
    print(max(0, max(dp)))
for t in range(int(input())):
    solve()