def get_ind(x):
    return ord(x) - ord("a")
def solve():
    n, q = map(int, input().split())
    a = input()
    b = input()
    # print("TEST")
    count_a = [[0 for i in range(26)] for i in range(n+1)]
    for i in range(n):
        for j in range(26):
            count_a[i+1][j] = count_a[i][j]
        count_a[i+1][get_ind(a[i])] = count_a[i][get_ind(a[i])] + 1
    
    count_b = [[0 for i in range(26)] for i in range(n+1)]
    for i in range(n):
        for j in range(26):
            count_b[i+1][j] = count_b[i][j]
        count_b[i+1][get_ind(b[i])] = count_b[i][get_ind(b[i])] + 1
    
    for i in range(q):
        l, r = map(int, input().split())
        ans = 0
        count_at = [0] * 26
        count_bt = [0] * 26
        for j in range(26):
            count_at[j] = (count_a[r][j] - count_a[l-1][j])
            count_bt[j] = (count_b[r][j] - count_b[l-1][j])
        # print(count_a)
        # print(count_b)
        # print(i)
        for j in range(26):
            if count_at[j] >= count_bt[j]:
                rem = count_at[j] - count_bt[j]
                ans += rem
                for k in range(j+1, 26):
                    if count_at[k] < count_bt[k]:
                        temp = min(rem, (count_bt[k] - count_at[k]))
                        count_at[k] = count_at[k] + temp
                        rem -= temp
            else:
                rem = count_bt[j] - count_at[j]
                ans += rem
                for k in range(j+1, 26):
                    if count_at[k] > count_bt[k]:
                        temp = min(rem, (count_at[k] - count_bt[k]))
                        count_bt[k] = count_bt[k] + temp
                        rem -= temp
        print(ans)

for t in range(int(input())):
    solve()