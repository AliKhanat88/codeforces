import sys
input = sys.stdin.readline

def count_4(x):
    temp = str(x)
    ans = 0
    while temp != "":
        if temp[0] == "4":
            temp = "3" + (len(temp) - 1) * "9"
        for i in range(int(temp[0])):
            if i == 4:
                continue
            else:
                ans += 9 ** (len(temp) - 1)
        temp = temp[1:]
    return ans

# print(count_4(13))
def solve():
    n = int(input())
    mini = n
    maxi = 100 * n
    while maxi > mini:
        mid = mini + (maxi - mini) // 2
        temp = count_4(mid)
        if temp >= n:
            maxi = mid
        else:
            mini = mid + 1
    print(maxi)


for t in range(int(input())):
    solve()