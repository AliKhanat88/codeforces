def solve():
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    s = input().strip()
    sum_arr = [0] * (n+1)
    for i in range(1, n+1):
        sum_arr[i] = sum_arr[i-1] + arr[i]
    
    left = 0
    right = n-1
    ans = 0
    while right > left:
        if s[left] == "L":
            while right > left:
                if s[right] == "R":
                    ans += (sum_arr[right + 1] - sum_arr[left])
                    right -= 1
                    break
                else:
                    right -= 1
        left += 1
    print(ans)
for t in range(int(input())):
    solve()