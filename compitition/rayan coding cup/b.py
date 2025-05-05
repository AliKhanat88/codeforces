
def solve():
    n, m, k = map(int, input().split())
    temp_s = list(input())
    s = temp_s[:]
    count = 0
    ans1 = [0] * n
    per = 0
    for i in range(n):
        if s[i] == "0":
            count += 1
        else:
            count = 0
        if count >= m:
            for j in range(i, min(i + k, n)):
                s[j] = "1"
            per += 1
            count = 0
        ans1[i] = per
    s = temp_s[:]
    count = 0
    ans2 = [0] * n
    per = 0
    for i in range(n-1, -1, -1):
        if s[i] == "0":
            count += 1
        else:
            count = 0
        if count >= m:
            for j in range(i, max(i - k, 0), -1):
                s[j] = "1"
            count = 0
            per += 1
        # print(per, i)
        ans2[i] = per
    # print(ans)
    # print(ans1)
    # print(ans2)
    # mini = float("inf")
    # for i in range(n):
    #     mini = min(mini, ans1[i] + ans2[i])
    print(min(ans2[0], ans1[n-1]))
    

for t in range(int(input())):
    solve()