def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    maxi00 = float("-inf")
    maxi10 = float("-inf")
    maxi01 = float("-inf")
    maxi11 = float("-inf")
    ans = 0
    for i in range(n):
        maxi00 = max(maxi00, -a[i]-b[i] - abs(a[i]-b[i]))
        maxi10 = max(maxi10, a[i]-b[i]- abs(a[i]-b[i]))
        maxi01 = max(maxi01, -a[i]+b[i]- abs(a[i]-b[i]))
        maxi11 = max(maxi11, a[i]+b[i]- abs(a[i]-b[i]))
        ans += abs(a[i] - b[i])
    maxi = 0

    for i in range(n):
        maxi = max(maxi, a[i] + b[i] + maxi00- abs(a[i] - b[i]), a[i] - b[i] + maxi10- abs(a[i] - b[i]), -a[i] + b[i] + maxi01- abs(a[i] - b[i]), -a[i]-b[i]+maxi11- abs(a[i] - b[i]))
    print(ans + maxi)


for t in range(int(input())):
    solve()