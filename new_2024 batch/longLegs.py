from math import isqrt

# def findMin(x, y):
#     mini = 99999999999999
#     for i in range(1, max(x, y)+ 1):
#         # print("i", i)
#         mini2 = 99999999999999
#         mini1 = 99999999999999
#         for j in range(1, i + 1):
#             mini1 = min(mini1, x // j + x % j)
#         for j in range(1, i + 1):
#             mini2 = min(mini2, y // j + y % j)
#         mini = min(mini, mini1 + mini2 + i - 1)
#         # print(mini2, mini, i)
#     return mini

def findMin(x, y):
    i = max(x, y)
    mini = i - 1 + 2
    temp1 = x
    temp2 = y
    while i >= 1:
        if temp1 >= temp2:
            cur = x // temp1
            cur += 1
            temp1 = x // cur
        else:
            cur = y // temp2
            cur += 1
            temp2 = y // cur
        if temp1 == 0 or temp2 == 0:
            break
        # print(temp1, temp2)
        i = max(temp1, temp2)
        mini = min(mini, i - 1 + x // temp1 + x % temp1 + y // temp2 + y % temp2)
    return mini

def solve():
    a, b = map(int, input().split())
    # print("TEST")
    # print(a, b)
    print(findMin(a, b))


for t in range(int(input())):
    solve()