from collections import defaultdict
from bisect import bisect_left

r = 0
c = 0
n = int(input())
arr = list(map(int, input().split()))
arr.pop(0)
temp = arr.pop(0)
stack = [temp]
dict = defaultdict(lambda:False)
t = 1
per = 0
while True:
    for num in arr:
        ind = bisect_left(stack, num)
        if per == None or ind != per + 1:
            if per != None:
                r += 1
                dict[stack[per]] = True
            if ind != 0 and ind != len(stack) and dict[stack[ind-1]] != True:
                r += 1
                c += 1
            if ind != 0:
                dict[stack[ind-1]] = True
            stack.insert(ind, num)
            c += 1
            per = ind
        elif ind == per + 1:
            stack.insert(ind, num)
            per = ind
    if t >= n:
        break
    dict[stack[per]] = True
    # print(dict)
    arr = list(map(int, input().split()))
    arr.pop(0)
    per = None
    t += 1

print(r, c)