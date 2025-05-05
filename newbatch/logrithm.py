from math import log as log1
import sys
input = sys.stdin.readline
def log(x, b):
    if b ** (int(log1(x, b))) > x:
        return int(log1(x, b)) - 1
    elif b ** (int(log1(x, b)) + 1) <= x:
        return int(log1(x, b))  + 1
    return int(log1(x, b))

arr = [0] * (61)
splitter = [None] * (61)
for i in range(2, 61):
    temp = int(log(2 ** i ,i))
    # print(i ** temp, 2 ** (i+1))
    if i ** (temp + 1) < 2 ** (i+1) and i ** (temp + 1) > 2 ** (i):
        arr[i] = (i ** (temp + 1) - (2 ** i)) * (temp) + (-(i ** (temp + 1)) + 2 ** (i+1)) * (temp + 1)
        splitter[i] = i ** ((temp + 1))
    else:
        arr[i] = (2 ** (i+1) - (2 ** i)) * (temp)
# print(arr)
for i in range(2, 61):
    arr[i] = arr[i-1] + arr[i]
# print(arr)
# print(splitter)
rem = 1000000007
def solve():
    l, r = map(int, input().split())
    sumi = 0
    templ = int(log(l ,int(log(l, 2))))
    tempr = int(log(r ,int(log(r, 2))))
    if int(log(l, 2)) == int(log(r, 2)):
        # print(1)
        if splitter[int(log(l, 2))] != None and splitter[int(log(l, 2))] > l and splitter[int(log(l, 2))] <= r:
            print(((splitter[int(log(l, 2))] - l) * templ + (r - splitter[int(log(l, 2))] + 1) * tempr) % rem)
        else:
            print(((r - l + 1) * templ) % rem)
    else:
        if splitter[int(log(l, 2))] != None and l < splitter[int(log(l, 2))]:
            # print(2)
            sumi += max(0, splitter[int(log(l, 2))] - l) * templ
            sumi += (2 ** (int(log(l, 2)) + 1) - splitter[int(log(l, 2))]) * int(log(splitter[int(log(l, 2))], int(log(l, 2))))
        else:
            sumi += (2 ** (int(log(l, 2)) + 1) - l) * templ
        # print(sumi)
        if splitter[int(log(r, 2))] != None and r >= splitter[int(log(r, 2))]:
            # print(3)
            sumi += max(0, r - splitter[int(log(r, 2))] + 1) * tempr
            sumi += ( - (2 ** int(log(r, 2))) + splitter[int(log(r, 2))]) * int(log(2 ** int(log(r, 2)), int(log(r, 2))))
        else:
            sumi += (r - 2 ** (int(log(r, 2))) + 1) * tempr
        # print(sumi)
        sumi += arr[int(log(r, 2)) - 1] - arr[int(log(l, 2))]
        print(sumi % rem)
for t in range(int(input())):
    solve()

