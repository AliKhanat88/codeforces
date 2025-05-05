import sys
input = sys.stdin.readline
from bisect import bisect_right

def solve():
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    s = list(input().strip())

    broken = []
    maxi = -1
    last = None
    for i in range(n):
        if arr[i] != i + 1:
            maxi = max(maxi, arr[i]-1)
            if last == None:
                last = i
        if i == maxi:
            broken.append((last, maxi))
            maxi = -1
            last = None
    # print(broken)
            
    stack = []
    for i in range(n):
        temp = i
        temp_index = bisect_right(broken, (temp, 100000000000)) - 1
        if temp_index != -1:
            if temp < broken[temp_index][1] and temp >= broken[temp_index][0] and s[temp] == "L" and s[temp+1] == "R":
                stack.append(temp)
            if temp <= broken[temp_index][1] and temp > broken[temp_index][0] and s[temp-1] == "L" and s[temp] == "R":
                stack.append(temp-1)
    # print(l, r)
    for i in range(q):
        temp = int(input()) - 1
        if s[temp] == "L":
            s[temp] = "R"
        else:
            s[temp] = "L"
        temp_index = bisect_right(broken, (temp, 100000000000)) - 1
        # print(temp, temp_index)
        if temp_index != -1:
            if temp < broken[temp_index][1] and temp >= broken[temp_index][0] and s[temp] == "L" and s[temp+1] == "R":
                stack.append(temp)
            if temp <= broken[temp_index][1] and temp > broken[temp_index][0] and s[temp-1] == "L" and s[temp] == "R":
                stack.append(temp-1)
        while len(stack) > 0:
            if s[stack[-1]] == "L" and s[stack[-1]+1] == "R":
                break
            else:
                stack.pop()
        if len(stack) == 0:
            print("YES")
        else:
            print("NO")




for t in range(int(input())):
    solve()