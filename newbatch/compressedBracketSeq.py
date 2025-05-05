def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    ans = 0
    # print("TEST")
    for i in range(1, n, 2):
        rem = arr[i]
        if rem >= arr[i-1]:
            ans += arr[i-1]
            rem -= arr[i-1]
        else:
            ans += rem
            rem = 0
            continue
        # print(rem, ans)
        temp = 0
        j = i - 2
        while j >= 0:
            temp -= arr[j]
            temp += arr[j-1]
            if temp >= 0:
                if temp > rem:
                    ans += rem + 1
                    break
                else:
                    ans += temp + 1
                    rem -= temp
                    temp = 0
            j -= 2


    print(ans)
# for t in range(int(input())):
solve()