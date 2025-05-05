from collections import Counter
inf = 999999999999
def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    mini = min(arr)
    arr.sort()
    arr_k = [0] * n
    for i in range(n):
        arr_k[i] = (arr[i] - mini) % (2 * k)


    # print("TEST")
    # print(arr)
    # print(arr_k)

    dict = Counter(arr_k)
    # print(dict)
    # print(mini_ab_k)

    mini_ab_k = (arr[-1] - mini) % (2 * k)
    mini = mini_ab_k
    start = arr[-1]
    ans = start
    for i in range(mini_ab_k, mini_ab_k - k, -1):
        if i < 0:
            temp = i + 2 * k
        else:
            temp = i
        if dict[temp] != 0:
            mini = temp
            ans = start
        start -= 1
    # print(mini)
    count = 0
    for i in range(mini, mini + k):
        count += dict[i]
        count += dict[i - 2 * k]
        if count >= n:
            print(ans)
            return
        ans += 1
    print(-1)
for t in range(int(input())):
    solve()