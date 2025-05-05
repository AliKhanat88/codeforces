def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    maxi = max(arr)
    sumi = sum(arr)
    # ans = 1
    for i in range(n, 1, -1):
        if maxi * i <= sumi + k:
            if sumi % i == 0:
                print(i)
                return
            elif i - (sumi % i) + sumi <= sumi + k:
                print(i)
                return 

    print(1)


for t in range(int(input())):
    solve()