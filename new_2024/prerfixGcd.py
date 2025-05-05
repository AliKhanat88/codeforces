from math import gcd

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    if n == 1:
        print(arr[0])
        return
    MAX = max(arr) + 1

    cnt = [0] * MAX
    occur = [0] * MAX
    for i in range(n):
        occur[arr[i]] += 1
    

    for i in range(2, MAX):
        cnt[i] += occur[i]
        for j in range(i + i, MAX, i):
            cnt[i] += occur[j]
    least = 1
    for i in range(MAX - 1, 1, -1):
        if cnt[i] == n:
            least *= i
            break
    # print(least)
    ans = min(arr)
    arr.remove(ans)
    count = 1
    sumi = ans
    while ans != least:
        for i in range(len(arr)):
            arr[i] = gcd(ans, arr[i])
        ans = min(arr)
        sumi += ans
        arr.remove(ans)
        count += 1
    print(sumi + (n - count) * least)


    # print(cnt[:21])

    
    # for i in range(n):
    #     for 


for t in range(int(input())):
    solve()