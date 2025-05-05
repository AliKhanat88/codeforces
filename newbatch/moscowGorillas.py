def solve():
    n = int(input())

    a = list(map(int, input().split()))

    b = list(map(int, input().split()))

    a_pair = [(a[i], i+1) for i in range(n)]

    b_pair = [(b[i], i+1) for i in range(n)]
    a_pair.sort()
    b_pair.sort()
    mini = min(a_pair[0][1], b_pair[0][1])
    maxi = max(a_pair[0][1], b_pair[0][1])
    # print(a_pair)
    # print(b_pair)
    # print(mini, maxi)
    count_a = [0] * (n+2)
    count_b = [0] * (n+2)
    ans = ((mini - 1) * mini) // 2 + ((n - maxi) * (n - maxi + 1)) // 2 + ((maxi - mini - 1) * (maxi - mini)) // 2
    for j in range(mini-1, maxi):
        count_a[a[j]] += 1
        count_b[b[j]] += 1
    # print(count_a)
    # print(count_b)
    if count_a[2] == count_b[2] and count_a[2] == 0:
        ans += 1
    # print(ans)
    for i in range(1, n):
        old_mini, old_maxi = mini, maxi
        if min(a_pair[i][1], b_pair[i][1]) >= mini and max(a_pair[i][1], b_pair[i][1]) <= maxi:
            pass

        elif a_pair[i][1] < mini and b_pair[i][1] > maxi:
            ans += ((mini - a_pair[i][1]) * (b_pair[i][1] - maxi) - 1)
            mini = a_pair[i][1]
            maxi = b_pair[i][1]

        elif b_pair[i][1] < mini and a_pair[i][1] > maxi:
            ans += ((mini - b_pair[i][1]) * (a_pair[i][1] - maxi) - 1)
            mini = b_pair[i][1]
            maxi = a_pair[i][1]

        elif a_pair[i][1] < mini and b_pair[i][1] < mini:
            ans += ((mini - max(a_pair[i][1], b_pair[i][1])) * (n - maxi + 1) - 1)
            mini = min(a_pair[i][1], b_pair[i][1])

        elif a_pair[i][1] > maxi and b_pair[i][1] > maxi:
            ans += ((min(a_pair[i][1], b_pair[i][1]) - maxi) * (mini) - 1)
            maxi = max(a_pair[i][1], b_pair[i][1])

        elif a_pair[i][1] >= mini and a_pair[i][1] <= maxi:
            mini = min(mini, b_pair[i][1])
            maxi = max(maxi, b_pair[i][1])
        elif b_pair[i][1] >= mini and b_pair[i][1] <= maxi: 
            mini = min(mini, a_pair[i][1])
            maxi = max(maxi, a_pair[i][1])
        for j in range(mini-1, old_mini-1):
            count_a[a[j]] += 1
            count_b[b[j]] += 1
        for j in range(old_maxi, maxi):
            count_a[a[j]] += 1
            count_b[b[j]] += 1
        if count_a[i+2] == count_b[i+2] and count_a[i+2] == 0:
            ans += 1
        # print(count_a)
        # print(count_b)
        # print(ans, i)
    print(ans)

    return ans


# for t in range(int(int(input()))):
if __name__ == "__main__":
    solve()