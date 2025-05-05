import sys
input = sys.stdin.readline
def give_pairs(x, slots):
    mult = x // slots
    rem = x % slots
    first = slots - rem
    ans = ((2 * (x - mult) + ((first-1) * (-mult))) / 2) * first * mult
    ans += ((2 * (mult + 1) + (slots - first - 2) * (mult+1)) / 2) * (slots - first - 1) * (mult+1)

    return int(ans)


# print(give_pairs(2, 2))
def solve():
    n, b, x = map(int, input().split())
    arr = list(map(int, input().split()))
    maxi = max(arr) + 1
    ans = [-(i - 1) * x for i in range(maxi)]
    ans[0] = -99999999

    # print(ans)
    add = [0] * (maxi + 1)
    for i in range(n):
        for j in range(1, arr[i]+1):
            ans[j] += (give_pairs(arr[i], j) * b)
        add[arr[i] +1] += give_pairs(arr[i], arr[i]) * b
    # print(ans)
    temp_add = 0
    maxi2 = 0
    for i in range(1, maxi):
        temp_add += add[i]
        maxi2 = max(maxi2, temp_add + ans[i])
    print(maxi2)
        
    # print("TEST")
    # print(new_maxi)
    # print(ind)
    


for t in range(int(input())):
    solve()