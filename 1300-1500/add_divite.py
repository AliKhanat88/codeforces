from math import log2, ceil
def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    mini = min(arr)
    maxi = max(arr)
    if maxi - mini == 0:
        print(0)
        return

    ans = ceil(log2(maxi - mini + 1))
    print(ans)
    if ans <= n:
        for i in range(ans):
            if mini % 2 == 1:
                mini = (mini+1) // 2
                maxi = (maxi+1) // 2
                print(1, end=" ")
            else:
                mini = (mini) // 2
                maxi = (maxi) // 2
                print(0, end=" ")
            # print(mini, maxi)
        print()






for t in range(int(input())):
    solve()