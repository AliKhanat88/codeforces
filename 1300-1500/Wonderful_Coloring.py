from collections import Counter
def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    c = Counter(arr)
    arr = [[i, arr[i], 0] for i in range(n)]
    arr.sort(key=lambda x:x[1])

    i = 0
    ans = 1
    while i < n:
        if c[arr[i][1]] >= k:
            temp = arr[i][1]
            temp_ans = 1
            while i < n and arr[i][1] == temp:
                if temp_ans <= k:
                    arr[i][2] = temp_ans
                    temp_ans += 1
                i += 1
        else:
            arr[i][2] = ans
            ans += 1
            if ans > k:
                ans = 1
            i += 1
        # print(arr, ans)
    # print(arr)
    i = n-1
    while ans != 1:
        if c[arr[i][1]] < k:
            arr[i][2] = 0
            ans -= 1
        i -= 1
    print_ans = [0] * n
    for num in arr:
        print_ans[num[0]] = str(num[2])
    print(" ".join(print_ans))
for t in range(int(input())):
    solve()